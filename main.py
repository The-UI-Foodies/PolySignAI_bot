#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from consts import *
import logging
import os
import numpy as np
import json
import emoji

from telegram import ForceReply, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

def inline_keyboard_builder() -> InlineKeyboardMarkup:

    language_keyboard = np.array(
        [
            InlineKeyboardButton(
                lang, 
                callback_data=lang,
            ) for lang in KEYBOARD_LANG_LIST
        ]
    )

    language_keyboard = language_keyboard.reshape(-1, NUM_LANGS_PER_ROW).tolist()
    
    return InlineKeyboardMarkup(language_keyboard)

def __init_user_data(context: ContextTypes.DEFAULT_TYPE):
    context.user_data["task_in_progress"] = None
    context.user_data["task_in_progress_msg_id"] = None
    context.user_data["task_in_progress_error_raised_msg_list"] = []

async def __clear_msgs(context: ContextTypes.DEFAULT_TYPE) -> None:
    for msg in context.user_data["task_in_progress_error_raised_msg_list"]:
        await msg.delete()

async def __print_src_or_dst_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE, direction_key: str, direction: str
):
    
    if direction_key in context.user_data:
        await update.message.reply_text(f"Selected {direction} language: {context.user_data[direction_key]}")
    
    else:
        await update.message.reply_text(
            f"No {direction} language selected yet.\nUse /src command to set the {direction} language"
        )


async def __is_there_in_progress_task(update: Update, context: ContextTypes.DEFAULT_TYPE, task_to_start: str) -> bool:

    if context.user_data["task_in_progress"] is not None:
    
        msg = await update.message.reply_text(
            text=f"Can't start {task_to_start} because there is another task in progress ({context.user_data['task_in_progress']})\n"
                f"Finish {context.user_data['task_in_progress']} first!",
            reply_to_message_id=context.user_data["task_in_progress_msg_id"]
        )

        context.user_data["task_in_progress_error_raised_msg_list"].append(update.message)
        context.user_data["task_in_progress_error_raised_msg_list"].append(msg)

        return True
    
    return False


async def src_or_dst_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE, task_to_start: str,
    lang_selection_task: str, command_message: str
) -> None:
    
    if await __is_there_in_progress_task(update, context, task_to_start):

        return

    context.user_data["task_in_progress"] = lang_selection_task

    keyboard = inline_keyboard_builder()
    
    msg = await update.message.reply_text(command_message, reply_markup=keyboard)

    context.user_data["task_in_progress_msg_id"] = msg.message_id


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    __init_user_data(context)

    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(HELP_MESSAGE)

### --- src --- ###

async def src_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await src_or_dst_command(
        update, context, 
        SRC_TASK_TO_START, SRC_LANG_SELECTION_TASK, SRC_COMMAND_MESSAGE
    )

async def select_language_src_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    query = update.callback_query
    
    context.user_data[SRC_LANG] = query.data
    
    await query.answer()
    
    await query.edit_message_text(
        text=f"Selected source language: {context.user_data[SRC_LANG]}",
        reply_markup=None # in order to hide the keyboard once a language has been selected
    )

    await __clear_msgs(context=context)
    
    __init_user_data(context)


async def print_src_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await __print_src_or_dst_command(update=update, context=context, direction_key=SRC_LANG, direction=SRC)

### --- src --- ###

### --- dst --- ###

async def dst_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await src_or_dst_command(
        update, context, 
        DST_TASK_TO_START, DST_LANG_SELECTION_TASK, DST_COMMAND_MESSAGE
    )


async def select_language_dst_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    query = update.callback_query
    
    context.user_data[DST_LANG] = query.data
    
    await query.answer()

    await query.edit_message_text(
        text=f"Selected destination language: {context.user_data[DST_LANG]}",
        reply_markup=None # in order to hide the keyboard once a language has been selected
    )
    
    await __clear_msgs(context=context)
    
    __init_user_data(context)


async def print_dst_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await __print_src_or_dst_command(
        update=update, context=context, direction_key=DST_LANG, direction=DST
    )

### --- dst --- ###

### --- src and dst --- ##

# TODO set src AND dst together

async def print_src_and_dst_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await __print_src_or_dst_command(update=update, context=context, direction_key=SRC_LANG, direction=SRC)
    await __print_src_or_dst_command(update=update, context=context, direction_key=DST_LANG, direction=DST)

### --- src and dst --- ##

### --- swap --- ###

async def swap_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    if DST_LANG in context.user_data:
        # TODO add possibility of selecting missing language if it has NOT been selected before
    
        dst_lang = context.user_data[DST_LANG]

    else:

        await update.message.reply_text(
            f"Can't swap languages because no destination language selected yet.\n"
            f"Use /dst command to set the destination language"
        )

        return

    if SRC_LANG in context.user_data:
        # TODO add possibility of selecting missing language if it has NOT been selected before
    
        src_lang = context.user_data[SRC_LANG]

    else:

        await update.message.reply_text(
            f"Can't swap languages because no source language selected yet.\n"
            f"Use /src command to set the source language"
        )

        return

    context.user_data[DST_LANG] = src_lang
    context.user_data[SRC_LANG] = dst_lang

    await update.message.reply_text(
            f"Source and destination language swapped!\n"
            f"Source language: {context.user_data[SRC_LANG]}\n"
            f"Destination language: {context.user_data[DST_LANG]}\n"
        )

### --- swap --- ###

### --- translation --- ###

async def text_translation_entry_point(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("text_translation_entry_point")

async def video_translation_entry_point(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("video_translation_entry_point")

async def audio_translation_entry_point(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("audio_translation_entry_point")


### --- translation --- ###

async def not_supported_type_entry_point(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("not_supported_type_entry_point")

async def query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    if context.user_data["task_in_progress"] == SRC_LANG_SELECTION_TASK:
        await select_language_src_handler(update, context)
    
    elif context.user_data["task_in_progress"] == DST_LANG_SELECTION_TASK:
        await select_language_dst_handler(update, context)


async def detect_wrong_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("detect_wrong_command")
    # TODO
    # NOTE it (probably) needs added support from BotFather: https://stackoverflow.com/questions/34457568/how-to-show-options-in-telegram-bot
    pass

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("src", src_command))
    application.add_handler(CommandHandler("dst", dst_command))
    application.add_handler(CommandHandler("swap", swap_command))
    application.add_handler(CommandHandler("langsrc", print_src_command))
    application.add_handler(CommandHandler("langdst", print_dst_command))
    application.add_handler(CommandHandler("lang", print_src_and_dst_command))
    application.add_handler(CallbackQueryHandler(query_handler))

    application.bot.set_my_commands(commands=[
        BotCommand("start", "Start the bot"),
        BotCommand("help", "Show the list of available commands"),
        BotCommand("src", "Set the source language"),
        BotCommand("dst", "Set the destination language"),
        BotCommand("swap", "Swap the source and destination languages"),
        BotCommand("langsrc", "Show the current source language"),
        BotCommand("langdst", "Show the current destination language"),
        BotCommand("lang", "Show the current source and destination languages"),
    ])

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_translation_entry_point))
    application.add_handler(MessageHandler(filters.VIDEO | filters.VIDEO_NOTE, video_translation_entry_point))
    application.add_handler(MessageHandler(filters.VOICE, audio_translation_entry_point))
    
    application.add_handler(MessageHandler(filters.COMMAND, detect_wrong_command))

    not_supported_filter = ~(filters.TEXT |
                             filters.VIDEO |filters.VIDEO_NOTE |
                             filters.VOICE)

    application.add_handler(MessageHandler(not_supported_filter, not_supported_type_entry_point))


    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()