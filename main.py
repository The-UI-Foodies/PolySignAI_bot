from io import BufferedReader
from consts import *
import logging
import os
import numpy as np
import emoji
import telegram
import whisper
import deepl
from langdetect import detect as lang_detector


from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
from dotenv import load_dotenv

import lang_keyboard

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DEEPL_TOKEN = os.getenv("DEEPL_TOKEN")


whisper_model = whisper.load_model('base')
translator = deepl.Translator(DEEPL_TOKEN)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

def __init_user_data(context: ContextTypes.DEFAULT_TYPE):
    context.user_data[SRC_LANG] = KEYBOARD_LANG_LIST[1]["text"]
    context.user_data[DST_LANG] = KEYBOARD_LANG_LIST[5]["text"]

async def post_init(application: Application):
    await application.bot.set_my_commands(commands=[
        BotCommand("start", "Start the bot"),
        BotCommand("help", "Get a quick overview of the bot's functionalities"),
        BotCommand("swap", "Swap the source and destination languages"),
        BotCommand("lang", "Show the current source and destination languages")
    ])
    

# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    __init_user_data(context)
    
    """Send a message when the command /start is issued."""
    await update.message.reply_text(WELCOME_MESSAGE)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(HELP_MESSAGE, parse_mode=telegram.constants.ParseMode.MARKDOWN)

### --- lang --- ###

async def lang_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = lang_keyboard.build_keyboard(context.user_data[SRC_LANG], context.user_data[DST_LANG])
    await update.message.reply_text(LANG_MESSAGE, reply_markup=keyboard)

async def swap_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    keyboard = lang_keyboard.swap_languages(query.message.reply_markup)
    await query.edit_message_reply_markup(keyboard)
    return await query.answer()

async def lang_selection_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    src, dst = lang_keyboard.get_selected_from_keyboard(query.message.reply_markup)

    lang, direction = query.data.split("_")
    if direction == "src":
        if dst == lang:
            keyboard = lang_keyboard.swap_languages(query.message.reply_markup)
        else:
            keyboard = lang_keyboard.build_keyboard(lang, dst)
    if direction == "dst":
        if src == lang:
            keyboard = lang_keyboard.swap_languages(query.message.reply_markup)
        else:
            keyboard = lang_keyboard.build_keyboard(src, lang)
    
    await query.edit_message_reply_markup(keyboard)
    return await query.answer()

async def done_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    src, dst = lang_keyboard.get_selected_from_keyboard(update.callback_query.message.reply_markup)
    context.user_data[SRC_LANG] = src
    context.user_data[DST_LANG] = dst
    await query.edit_message_text(LANG_DONE_MESSAGE, reply_markup=None)
    return await query.answer()

### --- lang --- ###

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
def is_signed(button_text: str):
    for obj in KEYBOARD_LANG_LIST:
        if button_text in obj.values():
            return not obj["is_spoken"]

def text_to_sign(text: str) -> BufferedReader:
    video = open("./dummy/translation.mp4", "rb")
    return video

def audio_to_sign(audio) -> BufferedReader:
    return text_to_sign("AUDIO_TO_SIGN_RESULT_PLACEHOLDER")

def text_to_text(text: str, src_lang, target_lang) -> dict:
    target_lang = LANGUAGE_DICT[target_lang]
    src_lang = LANGUAGE_DICT[src_lang]
    text_info = translator.translate_text(text, target_lang=target_lang)
    detected_src = text_info.detected_source_lang.lower()

    should_swap_langs = detected_src == target_lang
    if should_swap_langs:
        target_lang = src_lang

    translation = translator.translate_text(text, target_lang=target_lang)
    return {
        "translation": translation.text,
        "detected_src": translation.detected_source_lang,
        "is_swapped": should_swap_langs
    }

def audio_to_text(audio, src_lang, target_lang) -> dict:
    target_lang = LANGUAGE_DICT[target_lang]
    src_lang = LANGUAGE_DICT[src_lang]

    print("Starting transcribing")
    transcribe_info = whisper_model.transcribe(audio)
    print("Done transcribing")
    detected_src = transcribe_info["language"].lower()

    should_swap_langs = detected_src == target_lang
    if should_swap_langs:
        target_lang = src_lang
    
    translation = translator.translate_text(transcribe_info["text"], source_lang=detected_src, target_lang=target_lang)
    return {
        "translation": translation.text,
        "detected_src": detected_src,
        "is_swapped": should_swap_langs
    }

def sign_to_text(video: BufferedReader) -> str:
    return "SIGN_TO_TEXT_TRANSLATION_PLACEHOLDER"

def sign_to_sign(video: BufferedReader) -> BufferedReader:
    text = sign_to_text(video)
    video = text_to_sign(text)
    return video


async def text_translation_entry_point(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg_id = update.message.message_id
    src = context.user_data[SRC_LANG]
    dst = context.user_data[DST_LANG]

    # Error handling
    if is_signed(src) and is_signed(dst):
        await update.message.reply_text(
            MSG_SHOULD_BE_VIDEO_ERROR, 
            reply_to_message_id=msg_id
        )
        return
    
    # No errors detected
    if not is_signed(src) and not is_signed(dst):
        result = text_to_text(update.message.text, src, target_lang=dst)
        print(result)
        await update.message.reply_text(result["translation"], reply_to_message_id=msg_id)
    elif not is_signed(src):
        # Without swapping
        video = text_to_sign(update.message.text)
        await update.message.reply_video(video=video, supports_streaming=True, reply_to_message_id=msg_id)
    elif not is_signed(dst):
        # Swapping
        video = text_to_sign(update.message.text)
        await update.message.reply_video(video, reply_to_message_id=msg_id)

async def video_translation_entry_point(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg_id = update.message.message_id
    src = context.user_data[SRC_LANG]
    dst = context.user_data[DST_LANG]

    # Error handling
    if (not is_signed(src)) and (not is_signed(dst)):
        await update.message.reply_text(
            MSG_SHOULD_BE_TEXT_ERROR, 
            reply_to_message_id=msg_id
        )
        return

    # No errors detected
    if is_signed(src) and is_signed(dst):
        video = sign_to_sign(update.message.text)
        await update.message.reply_video(video=video, supports_streaming=True, reply_to_message_id=msg_id)
    elif is_signed(src):
        # Without swapping
        text = sign_to_text(update.message.text)
        await update.message.reply_text(text, reply_to_message_id=msg_id)
    elif is_signed(dst):
        # Swapping
        text = sign_to_text(update.message.text)
        await update.message.reply_text(text, reply_to_message_id=msg_id)
    

async def audio_translation_entry_point(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg_id = update.message.message_id
    src = context.user_data[SRC_LANG]
    dst = context.user_data[DST_LANG]

    # Error handling
    if is_signed(src) and is_signed(dst):
        await update.message.reply_text(
            MSG_SHOULD_BE_VIDEO_ERROR, 
            reply_to_message_id=msg_id
        )
        return
    
    # No errors detected
    file_info = await update.message.voice.get_file()
    file_path = f"./voice/{file_info.file_unique_id}.ogg"
    await file_info.download_to_drive(file_path)
    audio_data = whisper.load_audio(file_path)

    if not is_signed(src) and not is_signed(dst):
        result = audio_to_text(audio_data, src, dst)
        print(result)
        await update.message.reply_text(result["translation"], reply_to_message_id=msg_id)
    elif not is_signed(src):
        # Without swapping
        video = audio_to_sign(audio_data)
        await update.message.reply_video(video=video, supports_streaming=True, reply_to_message_id=msg_id)
    elif not is_signed(dst):
        # Swapping
        video = audio_to_sign(audio_data)
        await update.message.reply_video(video, reply_to_message_id=msg_id)

### --- translation --- ###

async def not_supported_type_entry_point(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("not_supported_type_entry_point")

async def query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    if "_src" in query.data or "_dst" in query.data:
        return await lang_selection_handler(update, context)
    
    if query.data == "Swap":
        return await swap_handler(update, context)

    if query.data == "Done":
        return await done_handler(update, context)

    return await query.answer()

async def detect_wrong_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "This command is not supported.\nValid options:\n" + HELP_MESSAGE,
        reply_to_message_id=update.message.message_id
        )

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).post_init(post_init).build()
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("swap", swap_command))
    application.add_handler(CommandHandler("lang", lang_command))
    application.add_handler(CallbackQueryHandler(query_handler))

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