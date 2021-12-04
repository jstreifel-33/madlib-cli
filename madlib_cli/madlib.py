import re

### CONSTANTS ###

PARTS_OF_SPEECH = "Adjective|Noun|Verb|Adverb|Interjection"

WELCOME_MESSAGE = """Welcome to the Python Madlib!
This tool will ask you for some words,
and then generate a funny text file
to show your friends!

Enter "start" to get started,
or "help" for additional commands.
"""

HELP_TEXT = """
Command options:
start - begin generating a madlib
view - display most recent madlib inside the console
changelib - select a new madlib
help - you are here
exit - quit the program
"""

INVALID_TEXT = """
Invalid command!
Enter "help" to see a list of valid commands.
"""

### USEFUL THINGS ###


def border_print(message, top_bott_bord=True):
    msg_list = message.splitlines()
    msg_width = 0

    # Determine max width line in message
    for line in msg_list:
        if len(line) > msg_width:
            msg_width = len(line)

    # Center lines based on pax width with 2 char whitepace padding
    for idx, line in enumerate(msg_list):
        msg_list[idx] = line.center(msg_width + 2)

    # Insert blank strings to list if top/bottom border not set False
    if top_bott_bord:
        msg_list.insert(0, "")
        msg_list.insert(len(msg_list), "")

    # Print each line of message, with added stars on side borders
    for line in msg_list:
        print(line.center(msg_width + 6, "*"))

    # White space
    print("")


### FILE HANDLING ###


def read_template(file):
    try:
        with open(file, "r") as f:
            contents = f.read()
            return contents
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template(template):
    # Extract parts of speech from template
    words_required = re.findall(PARTS_OF_SPEECH, template)

    # Replace parts of speech with empty string
    stripped_template = re.sub(PARTS_OF_SPEECH, "", template)

    return stripped_template, tuple(words_required)


def merge(template, words):
    return template.format(*words)


### GAME ACTIONS ###


def get_input(file="assets/dark_and_stormy_night_template.txt"):
    command = input("> ")
    cmd_process(command, file)
    get_input(file)


def generate_madlib(file):
    raw_template = read_template(file)
    template, words = parse_template(raw_template)

    user_words = []

    for word in words:
        response = input(f"\nEnter a(n) {word}: ")
        user_words.append(response)

    return merge(template, user_words)


def save_madlib(content):
    with open("assets/madlib_result.txt", "w") as f:
        f.write(content)
    print('\nMadlib generated successfully!\nEnter "view" to display!\n')


def select_madlib():
    pass


def cmd_process(cmd, file):
    if cmd == "exit":
        print("\nGoodbye!")
        exit()

    if cmd == "help":
        print(HELP_TEXT)
        return

    if cmd == "start":
        madlib = generate_madlib(file)
        save_madlib(madlib)
        return

    if cmd == "view":
        try:
            with open("assets/madlib_result.txt", "r") as f:
                contents = f.read()
                print(f"\nMost recent madlib:\n{contents}\n")
        except FileNotFoundError as e:
            print("\nError: no existing madlib at path assets/madlibresults.txt\n")
        return

    if cmd == "changelib":
        print("\nComing Soon!\n")
        return

    print(INVALID_TEXT)
    return


### GAME RUNNING SCRIPT ###


def start_game():
    border_print(WELCOME_MESSAGE)
    get_input()
