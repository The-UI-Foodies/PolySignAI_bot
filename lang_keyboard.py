import emoji
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from consts import KEYBOARD_LANG_LIST

def build_keyboard(src: str, dst: str) -> InlineKeyboardMarkup:
    temp_lang_list = [lang_obj["text"] for lang_obj in KEYBOARD_LANG_LIST]

    language_keyboard = [
            [
                InlineKeyboardButton(
                lang, 
                callback_data=lang + "_src",
                ),
                InlineKeyboardButton(
                    lang, 
                    callback_data=lang + "_dst",
                )
            ] for lang in temp_lang_list
        ]
    
    for row in language_keyboard:
        if src == row[0].text:
            text_selected = emoji.emojize(":check_mark_button: " + row[0].text)
            row[0] = InlineKeyboardButton(
                    text_selected, 
                    callback_data=text_selected,
            )
        if dst == row[1].text:
            text_selected = emoji.emojize(":check_mark_button: " + row[1].text)
            row[1] = InlineKeyboardButton(
                    text_selected, 
                    callback_data=text_selected,
            )
    
    language_keyboard.append([InlineKeyboardButton("Swap", callback_data="Swap")])
    language_keyboard.append([InlineKeyboardButton("Done", callback_data="Done")])
    
    return InlineKeyboardMarkup(language_keyboard)

def get_selected_from_keyboard(keyboard: InlineKeyboardMarkup) -> (str, str):
    keyboard = keyboard.to_dict()
    keyboard = keyboard["inline_keyboard"]
    keyboard.pop()
    keyboard.pop()
    for row in keyboard:
        if row[0]["text"][:1] == emoji.emojize(":check_mark_button:"):
            src = row[0]["text"][2:]
        if row[1]["text"][:1] == emoji.emojize(":check_mark_button:"):
            dst = row[1]["text"][2:]
    return src, dst

def swap_languages(keyboard: InlineKeyboardMarkup) -> InlineKeyboardMarkup:
    src, dst = get_selected_from_keyboard(keyboard)
    return build_keyboard(src=dst, dst=src)

