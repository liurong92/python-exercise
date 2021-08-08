"""
Update the "What Did the Cat Say" program from an earlier section so that it can be run directly
or imported as a module. When it runs as a program is should prompt for input and display a cat
"saying" what was provided by the user. Place the input provided by the user inside a speech
bubble. Make the speech bubble expand or contract to fit around the input provided by the user.
Sample output when run interactively:
_______________________
< Pet me and I will purr. >
­­­­­­­­­­­­­­­­­­­­­­­
/
/\_/\ /
( o.o )
> ^ <
Next, create a new program called cat_talk.py that imports the cat_say module. Use a function
from the cat_say() module to display various messages to the screen.
Sample output when used as a module:
________
< Feed me. >
­­­­­­­­
/
/\_/\ /
( o.o )
> ^ <
_______
< Pet me. >
­­­­­­­
/
/\_/\ /
( o.o )
> ^ <
"""

from cat_talk import cat_say


def main():
    cat_say('Feed me.')
    cat_say('Pet me.')
    cat_say('Purr. Purr.')


if __name__ == '__main__':
    main()
