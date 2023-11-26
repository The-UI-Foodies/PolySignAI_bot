HELP_MESSAGE = "- /start:  Start\n" \
               "- /swap:  Swap source and destination languages\n" \
               "- /src:  Change source language (auto for detect language)\n" \
               "- /dest:  Change destination language\n" \
               "- /langs:  Show selected languages\n" \
               "- /fav:  Favorites setting (add or remove languages from favorites lists)\n" \
               "- /cancel:  Cancel the current operation\n" \
               "- /contact:  Contact with admin %s"

SRC_COMMAND_MESSAGE  = "Select the language to translate from:"
DEST_COMMAND_MESSAGE = "Select the language to translate to:"

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

KEYBOARD_LANG_LIST = [
    f"Italian {ITALIAN_FLAG_EMOJI}", 
    f"English {ENGLISH_FLAG_EMOJI}",
    f"French {FRENCH_FLAG_EMOJI}",
    f"German {GERMAN_FLAG_EMOJI}",
    f"Spanish {SPANISH_FLAG_EMOJI}",
    f"Italian Sign Language (LIS) {ITALIAN_FLAG_EMOJI} {OPEN_HANDS_EMOJI}",
    f"British Sign Language (BSL) {ENGLISH_FLAG_EMOJI} {OPEN_HANDS_EMOJI}",
    f"German Sign Language (DGS) {GERMAN_FLAG_EMOJI} {OPEN_HANDS_EMOJI}",
    f"Spanish Sign Language (LSE) {SPANISH_FLAG_EMOJI} {OPEN_HANDS_EMOJI}",
    f"American Sign Language (ASL) {US_FLAG_EMOJI} {OPEN_HANDS_EMOJI}",
]
