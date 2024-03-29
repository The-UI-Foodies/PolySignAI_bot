import iso639

# TODO update it with our command!

DATE_FORMAT = "%d/%m/%Y %H:%M:%S"

REQUIRED_DIRS = ["poses", "voice", "video"]

OK_EMOJI = "\u2705"
GENIE_EMOJI = "\U0001f9de\u200D\u2642\uFE0F"

MSG_SET_LANG = f"{GENIE_EMOJI} Please select a source (left) and destination (right) language by tapping on the appropriate buttons. {GENIE_EMOJI}"
MSG_LANG_SET = OK_EMOJI + "\nFrom now on, the bot will translate from {0} to {1}"

ERROR_EMOJI = "\u274C"
WARN_EMOJI = "\u26A0\uFE0F"

MSG_SHOULD_BE_VIDEO_WARN = WARN_EMOJI + " Selected {0} source language requires to translate from a video!\nAssuming you want to translate from {1}"
MSG_SHOULD_BE_TEXT_WARN = WARN_EMOJI + " Selected {0} source language requires to translate from an audio or a text!\nAssuming you want to translate from {1}"

OPS_EMOJI = "\U0001f92d"
NOT_AVAILABLE_EMOJI = "\U0001f636\u200D\U0001f32b\uFE0F"
PLEASE_HANDS_EMOJI = "\U0001f64f\U0001f3fc"

MSG_WHISPER_UNABLE_TO_TRANSCRIBE = f"{OPS_EMOJI} We can't hear your audio very well... could you try to speak louder, please?"
MSG_WHISPER_FAIL = f"{NOT_AVAILABLE_EMOJI} Audio transcribing service seems to be offline, please try again later {PLEASE_HANDS_EMOJI}\n\nIn the meantime, here's a nice GIF for you..."
MSG_DEEPL_FAIL = f"{NOT_AVAILABLE_EMOJI} Text translation service seems to be offline, please try again later {PLEASE_HANDS_EMOJI}\n\nIn the meantime, here's a nice GIF for you..."
MSG_SIGNMT_FAIL = f"{NOT_AVAILABLE_EMOJI} Sign translation service seems to be offline, please try again later {PLEASE_HANDS_EMOJI}\n\nIn the meantime, here's a nice GIF for you..."
MSG_POSE_FAIL = f"{OPS_EMOJI} We can't compose the translation into sign language... could you try again, please?"

# If you want to add some task, you gotta add form the last position
TASKS = ["SELECT_LANGUAGE_DST", "SELECT_LANGUAGE_SRC"]

NUM_LANGS_PER_ROW = 2

ITALIAN_FLAG_EMOJI = "\U0001f1ee\U0001f1f9"
ENGLISH_FLAG_EMOJI = "\U0001f1ec\U0001f1e7"
FRENCH_FLAG_EMOJI  = "\U0001f1eb\U0001f1f7"
GERMAN_FLAG_EMOJI  = "\U0001f1e9\U0001f1ea"
SPANISH_FLAG_EMOJI = "\U0001f1ea\U0001f1f8"
US_FLAG_EMOJI      = "\U0001f1fa\U0001f1f8"

OPEN_HANDS_EMOJI = "\U0001f450"
SPEAK_EMOJI = "\U0001f5e3\uFE0F"

HOURGLASS_EMOJI = "\u23F3"

TRANSCRIBING_EMOJI = "\u270D\U0001f3fb"

SL_TRANSLATION_EMOJI = "\U0001f90c\U0001f3fc"
SAD_EMOJI = "\u2639\uFE0F"
SAD_EMOJI_2 = "\U0001f614"

SRC_TASK_TO_START = "source language selection"
DST_TASK_TO_START = "destination language selection"

SRC_LANG_SELECTION_TASK = "Source language selection"
DST_LANG_SELECTION_TASK = "Destination language selection"

SRC_LANG = "src_lang"
SRC = "source"

DST_LANG = "dst_lang"
DST = "destination"

# Error list


TEXT_TO_SIGNED_BASE_URL = "https://us-central1-sign-mt.cloudfunctions.net/spoken_text_to_signed_pose"

KEYBOARD_LANG_LIST = [
    {"text": f"Italian {ITALIAN_FLAG_EMOJI}{SPEAK_EMOJI}", "is_spoken": True},
    {"text": f"English {ENGLISH_FLAG_EMOJI}{SPEAK_EMOJI}", "is_spoken": True},
    {"text": f"French {FRENCH_FLAG_EMOJI}{SPEAK_EMOJI}", "is_spoken": True},
    {"text": f"German {GERMAN_FLAG_EMOJI}{SPEAK_EMOJI}", "is_spoken": True},
    {"text": f"Spanish {SPANISH_FLAG_EMOJI}{SPEAK_EMOJI}", "is_spoken": True},
    {"text": f"Italian Sign Lang{ITALIAN_FLAG_EMOJI}{OPEN_HANDS_EMOJI}", "is_spoken": False},
    {"text": f"American Sign Lang{US_FLAG_EMOJI}{OPEN_HANDS_EMOJI}", "is_spoken": False},
    {"text": f"French Sign Lang{FRENCH_FLAG_EMOJI}{OPEN_HANDS_EMOJI}", "is_spoken": False},
    {"text": f"German Sign Lang{GERMAN_FLAG_EMOJI}{OPEN_HANDS_EMOJI}", "is_spoken": False},
    {"text": f"Spanish Sign Lang{SPANISH_FLAG_EMOJI}{OPEN_HANDS_EMOJI}", "is_spoken": False},
]

LANGUAGE_DICT = {
    f"Italian {ITALIAN_FLAG_EMOJI}{SPEAK_EMOJI}": "it",
    f"English {ENGLISH_FLAG_EMOJI}{SPEAK_EMOJI}": "en",
    f"French {FRENCH_FLAG_EMOJI}{SPEAK_EMOJI}": "fr",
    f"German {GERMAN_FLAG_EMOJI}{SPEAK_EMOJI}": "de",
    f"Spanish {SPANISH_FLAG_EMOJI}{SPEAK_EMOJI}": "es",
    f"Italian Sign Lang{ITALIAN_FLAG_EMOJI}{OPEN_HANDS_EMOJI}": "ise", # This "language code" is used by sign.mt API
    f"American Sign Lang{US_FLAG_EMOJI}{OPEN_HANDS_EMOJI}": "bfi",
    f"French Sign Lang{FRENCH_FLAG_EMOJI}{OPEN_HANDS_EMOJI}": "fsl",
    f"German Sign Lang{GERMAN_FLAG_EMOJI}{OPEN_HANDS_EMOJI}": "gsg",
    f"Spanish Sign Lang{SPANISH_FLAG_EMOJI}{OPEN_HANDS_EMOJI}": "ssp",
}

LANGUAGE_DICT_REVERSED = {
    "it": f"Italian {ITALIAN_FLAG_EMOJI}{SPEAK_EMOJI}",
    "en": f"English {ENGLISH_FLAG_EMOJI}{SPEAK_EMOJI}",
    "fr": f"French {FRENCH_FLAG_EMOJI}{SPEAK_EMOJI}",
    "de": f"German {GERMAN_FLAG_EMOJI}{SPEAK_EMOJI}",
    "es": f"Spanish {SPANISH_FLAG_EMOJI}{SPEAK_EMOJI}",
    "ise": f"Italian Sign Lang{ITALIAN_FLAG_EMOJI}{OPEN_HANDS_EMOJI}",
    "ase": f"American Sign Lang{US_FLAG_EMOJI}{OPEN_HANDS_EMOJI}",
    "fsl": f"French Sign Lang{FRENCH_FLAG_EMOJI}{OPEN_HANDS_EMOJI}",
    "gsg": f"German Sign Lang{GERMAN_FLAG_EMOJI}{OPEN_HANDS_EMOJI}",
    "ssp": f"Spanish Sign Lang{SPANISH_FLAG_EMOJI}{OPEN_HANDS_EMOJI}",
}

SPOKEN_TO_SIGNED = {
    f"Italian {ITALIAN_FLAG_EMOJI}{SPEAK_EMOJI}": f"Italian Sign Lang{ITALIAN_FLAG_EMOJI}{OPEN_HANDS_EMOJI}",
    f"English {ENGLISH_FLAG_EMOJI}{SPEAK_EMOJI}": f"American Sign Lang{US_FLAG_EMOJI}{OPEN_HANDS_EMOJI}",
    f"French {FRENCH_FLAG_EMOJI}{SPEAK_EMOJI}": f"French Sign Lang{FRENCH_FLAG_EMOJI}{OPEN_HANDS_EMOJI}",
    f"German {GERMAN_FLAG_EMOJI}{SPEAK_EMOJI}": f"German Sign Lang{GERMAN_FLAG_EMOJI}{OPEN_HANDS_EMOJI}",
    f"Spanish {SPANISH_FLAG_EMOJI}{SPEAK_EMOJI}": f"Spanish Sign Lang{SPANISH_FLAG_EMOJI}{OPEN_HANDS_EMOJI}"
}

SIGNED_TO_SPOKEN = {v: k for k, v in SPOKEN_TO_SIGNED.items()}


SUPPORTED_LANGUAGES_ISO_CODES = list(LANGUAGE_DICT_REVERSED.keys())
SUPPORTED_LANGUAGES_ISO_NAME = list(LANGUAGE_DICT.keys())[:5] # showing only spoken languages, NOT signed ones
SUPPORTED_LANGUAGES_STR = ", ".join(SUPPORTED_LANGUAGES_ISO_NAME)

SUPPORTED_LANGUAGES_DEEPL_ISO_CODES = [
    'bg', 'cs', 'da', 'de', 'el', 'en', 'es', 'et', 'fi', 'fr', 'hu', 'id', 
    'it', 'ja', 'ko', 'lt', 'lv', 'nb', 'nl', 'pl', 'pt', 'ro', 'ru', 'sk', 
    'sl', 'sv', 'tr', 'uk', 'zh'
]


SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "Actions speak louder than words.",
    "Where there's smoke, there's fire.",
    "Every cloud has a silver lining.",
    "Don't count your chickens before they hatch.",
    "All that glitters is not gold.",
    "The early bird catches the worm.",
    "When in Rome, do as the Romans do.",
    "Two wrongs don't make a right.",
    "Better late than never.",
    "A picture is worth a thousand words.",
    "You can't judge a book by its cover.",
    "When the going gets tough, the tough get going.",
    "Honesty is the best policy.",
    "The pen is mightier than the sword.",
    "Actions speak louder than words.",
    "Where there is a will, there is a way.",
    "Fortune favors the bold.",
    "Rome wasn't built in a day."
]

HI_HAND = "\U0001f596\U0001f3fc"
HEART_EMOJI = "\U0001f9e1"
HUGGING_FACE_EMOJI = "\U0001f917"

NEWLINE = "\n"

COOL_EMOJI = "\U0001f60e"

WELCOME_MESSAGE = f"{HI_HAND} Welcome to PolySignAI, a Telegram Bot to perform spoken-to-sign, sign-to-spoken and sign-to-sign translations in the following languages:\n{NEWLINE.join(list(LANGUAGE_DICT.keys()))}\n\n"\
    f"Use the command /help to see all details about available Bot commands.\n\n"\
    f"Come find us on [GitHub](https://github.com/The-UI-Foodies) {HUGGING_FACE_EMOJI}\n\n"\
    f"Made with {HEART_EMOJI} by [Daniele](https://github.com/dansolombrino), [Emanuele](https://github.com/emavola), [Ilaria](https://github.com/iladesio) and [Paolo](https://github.com/ppbevilacqua)\n\n"\
    f"Powered by [Sign Translate](https://github.com/sign/translate)"

HELP_MESSAGE = f"""
{HI_HAND} Welcome to PolySignAI, a Telegram Bot to perform spoken-to-sign, sign-to-spoken and sign-to-sign translations

*Available commands:*

- /start - Starts the bot 
- /help - Gets help using the bot 
- /lang - Sets source and destination languages 
- /swap - Swaps the source and destination languages 

*Usage:*

Set desired source and destination languages and *simply message* the bot to translate your messages!

If you select {list(LANGUAGE_DICT.keys())[2]} and send a message in {list(LANGUAGE_DICT.keys())[3]} PolySignAI will still be able to perform the translation! {COOL_EMOJI}

- To translate from a spoken language, simply send a text or an audio message.

- To translate from a signed language, simply send a video.

If you set a spoken source language, like {list(LANGUAGE_DICT.keys())[4]}, but you send a video, PolySignAI will assume you want to translate from the *corresponding* signed language {list(LANGUAGE_DICT.keys())[9]}

If you set a signed source language, like {list(LANGUAGE_DICT.keys())[7]}, but you send a video, PolySignAI will assume you want to translate from the *corresponding* spoken language {list(LANGUAGE_DICT.keys())[2]}

*Examples:*

- To translate "Hello, world!" from {list(LANGUAGE_DICT.keys())[1]} to {list(LANGUAGE_DICT.keys())[0]}, simply type "Ciao, mondo!" or record a voice message saying it.

- To translate from any supported signed language, simply send a video where you sign in sign language
"""