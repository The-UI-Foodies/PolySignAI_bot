HELP_MESSAGE = "- /start:  Start\n" \
               "- /swap:  Swap source and destination languages\n" \
               "- /src:  Change source language (auto for detect language)\n" \
               "- /dest:  Change destination language\n" \
               "- /langs:  Show selected languages\n" \
               "- /fav:  Favorites setting (add or remove languages from favorites lists)\n" \
               "- /cancel:  Cancel the current operation\n" \
               "- /contact:  Contact with admin %s"

SRC_COMMAND_MESSAGE = "Source language:"
DEST_COMMAND_MESSAGE = "Destination language:"

# If you want to add some task, you gotta add form the last position
TASKS = ["SELECT_LANGUAGE_DST", "SELECT_LANGUAGE_SRC"]

KEYBOARD_LANG_DICT = {
                        "Italian" : {"lang" : "it", "type": "spoken"},
                        "English": {"lang" : "en", "type": "spoken"},
                        "LIS": {"lang" : "lis", "type": "signed"},
                        "ASL": {"lang" : "asl", "type": "signed"}
                    }
