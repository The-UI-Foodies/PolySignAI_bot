# TODO update it with our command!

WELCOME_MESSAGE = "Welcome to PolySignAI!"

HELP_MESSAGE = """
This bot can translate text, audio, and video between multiple signed and spolen languages!

*Available commands:*

- /start - Start the bot
- /help - Get help using the bot
- /src - Set the source language
- /dst - Set the destination language
- /lang_src - Print the selected source language
- /lang_dst - Print the selected destination language
- /swap - Swap the source and destination languages

*Usage:*

- To translate text, simply send the text you want to translate as a message.
- To translate audio, send an audio message.
- To translate video, send a video message.

*Examples:*

- To translate "Hello, world!" from English to Italian, type "Ciao, mondo!"
- To translate an audio recording of a speech from French to Spanish, send the audio message.
- To translate a video of a lecture from German to Chinese, send the video message.
"""

LANG_MESSAGE = "LANG_MESSAGE_PLACEHOLDER"
LANG_DONE_MESSAGE = "LANG_DONE_MESSAGE_PLACEHOLDER"

MSG_SHOULD_BE_VIDEO_ERROR = "MSG_SHOULD_BE_VIDEO_ERROR"
MSG_SHOULD_BE_TEXT_ERROR = "MSG_SHOULD_BE_TEXT_ERROR"

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

SRC_TASK_TO_START = "source language selection"
DST_TASK_TO_START = "destination language selection"

SRC_LANG_SELECTION_TASK = "Source language selection"
DST_LANG_SELECTION_TASK = "Destination language selection"

SRC_LANG = "src_lang"
SRC = "source"

DST_LANG = "dst_lang"
DST = "destination"

TEXT_TO_SIGNED_BASE_URL = "https://us-central1-sign-mt.cloudfunctions.net/spoken_text_to_signed_pose"

KEYBOARD_LANG_LIST = [
    {"text": f"Italian {ITALIAN_FLAG_EMOJI}", "is_spoken": True},
    {"text": f"English {ENGLISH_FLAG_EMOJI}", "is_spoken": True},
    {"text": f"French {FRENCH_FLAG_EMOJI}", "is_spoken": True},
    {"text": f"German {GERMAN_FLAG_EMOJI}", "is_spoken": True},
    {"text": f"Spanish {SPANISH_FLAG_EMOJI}", "is_spoken": True},
    {"text": f"Italian Sign Lang{ITALIAN_FLAG_EMOJI}{OPEN_HANDS_EMOJI}", "is_spoken": False},
    {"text": f"British Sign Lang{ENGLISH_FLAG_EMOJI}{OPEN_HANDS_EMOJI}", "is_spoken": False},
    {"text": f"German Sign Lang{GERMAN_FLAG_EMOJI}{OPEN_HANDS_EMOJI}", "is_spoken": False},
    {"text": f"Spanish Sign Lang{SPANISH_FLAG_EMOJI}{OPEN_HANDS_EMOJI}", "is_spoken": False},
    {"text": f"American Sign Lang{US_FLAG_EMOJI}{OPEN_HANDS_EMOJI}", "is_spoken": False},
]

LANGUAGE_DICT = {
    f"Italian {ITALIAN_FLAG_EMOJI}": "it",
    f"English {ENGLISH_FLAG_EMOJI}": "en",
    f"French {FRENCH_FLAG_EMOJI}": "fr",
    f"German {GERMAN_FLAG_EMOJI}": "de",
    f"Spanish {SPANISH_FLAG_EMOJI}": "es",
    f"Italian Sign Lang{ITALIAN_FLAG_EMOJI}{OPEN_HANDS_EMOJI}": "ise", # This "language code" is used by sign.mt API
    f"British Sign Lang{ENGLISH_FLAG_EMOJI}{OPEN_HANDS_EMOJI}": "bfi",
    f"German Sign Lang{GERMAN_FLAG_EMOJI}{OPEN_HANDS_EMOJI}": "gsg",
    f"Spanish Sign Lang{SPANISH_FLAG_EMOJI}{OPEN_HANDS_EMOJI}": "ssp",
    f"American Sign Lang{US_FLAG_EMOJI}{OPEN_HANDS_EMOJI}": "ase",
}

LANGUAGE_DICT_REVERSED = {
    "it": f"Italian {ITALIAN_FLAG_EMOJI}",
    "en": f"English {ENGLISH_FLAG_EMOJI}",
    "fr": f"French {FRENCH_FLAG_EMOJI}",
    "de": f"German {GERMAN_FLAG_EMOJI}",
    "es": f"Spanish {SPANISH_FLAG_EMOJI}",
    "ise": f"Italian Sign Lang{ITALIAN_FLAG_EMOJI}{OPEN_HANDS_EMOJI}",
    "bfi": f"British Sign Lang{ENGLISH_FLAG_EMOJI}{OPEN_HANDS_EMOJI}",
    "gsg": f"German Sign Lang{GERMAN_FLAG_EMOJI}{OPEN_HANDS_EMOJI}",
    "ssp": f"Spanish Sign Lang{SPANISH_FLAG_EMOJI}{OPEN_HANDS_EMOJI}",
    "ase": f"American Sign Lang{US_FLAG_EMOJI}{OPEN_HANDS_EMOJI}",
}

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
