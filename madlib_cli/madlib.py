import re

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
help - you are here
exit - quit the program
"""

INVALID_TEXT = """
Invalid command!
Enter "help" to see a list of valid commands.
"""


class FileNotFoundError(Exception):
    def __init__(self):
        super().__init__()


def border_print(message, top_bott_bord=True):
  msg_list = message.splitlines()
  msg_width = 0

  #Determine max width line in message
  for line in msg_list:
    if len(line) > msg_width:
      msg_width = len(line)

  #Center lines based on pax width with 2 char whitepace padding
  for idx, line in enumerate(msg_list):
    msg_list[idx] = line.center(msg_width + 2)

  #Insert blank strings to list if top/bottom border not set False
  if top_bott_bord:
    msg_list.insert(0,'')
    msg_list.insert(len(msg_list), '')

  #Print each line of message, with added stars on side borders
  for line in msg_list:
    print(line.center(msg_width + 6, '*'))
  
  #White space
  print('')


def read_template(file):
    with open(file, "r") as f:
        contents = f.read()
        return contents


def parse_template(template):
    # Extract parts of speech from template
    words_required = re.findall(PARTS_OF_SPEECH, template)

    # Replace parts of speech with empty string
    stripped_template = re.sub(PARTS_OF_SPEECH, "", template)
    
    return stripped_template, tuple(words_required)


def merge(template, words):
    return template.format(*words)


def get_input():
    while True:
        command = input('> ')
        cmd_process(command)
    

def cmd_process(cmd):
    if cmd == 'exit':
        exit()

    if cmd == 'help':
        print(HELP_TEXT)
        return

    print(INVALID_TEXT)
    return


# GAME RUNNING SCRIPT

border_print(WELCOME_MESSAGE)
get_input()
