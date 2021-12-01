WELCOME_MESSAGE = '''Welcome to the Python Madlib!
This tool will ask you for some words,
and then generate a funny text file
to show your friends!

Enter "start" to get started,
or "help" for additional commands.'''

HELP_TEXT = '''Command options:
start - begin generating a madlib
view - display most recent madlib inside the console
help - you are here
exit - quit the program'''



def read_template(file):
    with open(file, 'r') as f:
        contents = f.read()
        return contents


def parse_template():
    pass

def merge():
    pass

