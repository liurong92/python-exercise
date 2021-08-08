"""
Create a dictionary that contains a list of people and one interesting fact about each of them.
Display each person and their interesting fact to the screen. Next, change a fact about one of
the people. Also add an additional person and corresponding fact. Display the new list of people
and facts. Run the program multiple times and notice if the order changes.
Sample output:
Jeff: Is afraid of clowns.
David: Plays the piano.
Jason: Can fly an airplane.

Jeff: Is afraid of heights.
David: Plays the piano.
Jason: Can fly an airplane.
Jill: Can hula dance.
"""


def __print__(facts):
    for fact_key, fact_value in facts.items():
        print('{0}: {1}'.format(fact_key, fact_value))


facts = {
    'Jeff': 'Is afraid of clowns.',
    'David': 'Plays the piano.',
    'Jason': 'Can fly an airplane.'
}
__print__(facts)
print()

facts['Jeff'] = 'Is afraid of heights.'
facts['Jill'] = 'Can hula dance.'
__print__(facts)
