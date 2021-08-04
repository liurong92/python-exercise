'''
Create a fill in the blank word game. Prompt the user to enter a noun, verb, and an adjective.
Use those responses to fill in the blanks and display the story.
Write a short story. Remove a noun, verb, and an adjective.
Create a function to get the input from the user.
Create a function that fills in the blanks in the story you created.
Ensure each function contains a docstring.
After the noun, verb, and adjective have been collected from the user, display the story using
their input.
'''


def __get_word__(word_type):
    if word_type.lower() == 'adjective':
        a_or_an = 'an'
    else:
        a_or_an = 'a'
    return input('Please input a word that is {0} {1}: '.format(a_or_an, word_type))


def __create_story__():
    noun = __get_word__('noun')
    verb = __get_word__('verb')
    adjective = __get_word__('adjective')
    print('\nFirst word is {0},\nsecond word is {1},\nlast word is {2}'.format(noun, verb, adjective))

__create_story__()
