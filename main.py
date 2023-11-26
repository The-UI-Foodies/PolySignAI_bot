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

from telegram import ForceReply, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
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

def my_update_dict(dict: dict, key, value):
    dict.update({key:value})
    return dict


def inline_keyboard_builder(is_src: bool, make_selected=0) -> InlineKeyboardMarkup:

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

# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(HELP_MESSAGE)

async def src_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = inline_keyboard_builder(True)
    
    await update.message.reply_text(
        SRC_COMMAND_MESSAGE,
        reply_markup=keyboard
    )
    
async def dest_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await None

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

async def select_language_src_handler(update: Update, context: ContextTypes.DEFAULT_TYPE, data:dict) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        f"Selected source language: {data['lang']}\nNow select the destination:", 
        reply_markup=inline_keyboard_builder(is_src = False)
    )

async def select_language_dst_handler(update: Update, context: ContextTypes.DEFAULT_TYPE, data:dict) -> None:
    query = update.callback_query
    print()
    print(update)
    print()
    print()
    await query.answer()
    await query.edit_message_text(f"Ciao")

async def query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    #if query.data == "Disabled":

    print()
    print()
    print(query.data)
    print()
    print()
    data = json.loads(query.data)

    if data["task"] ==  "SELECT_LANGUAGE_SRC":
        await select_language_src_handler(update, context, data)
    elif data["task"] == "SELECT_LANGUAGE_DST":
        await select_language_dst_handler(update, context, data)
    
    

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("src", src_command))
    application.add_handler(CallbackQueryHandler(query_handler))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()