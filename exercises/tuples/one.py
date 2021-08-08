"""
Create a list of airports that includes a series of tuples containing an airport's name and its code.
Loop through the list and utilize tuple assignment. Use one variable to hold the airport name and
another variable to hold the airport code. Display the airport's name and code to the screen.
Sample output:
The code for O’Hare International Airport is ORD.
The code for Los Angeles International Airport is LAX.
The code for Dallas/Fort Worth International Airport is DFW.
The code for Denver International Airport is DEN.
"""

def __print__(airports):
    for (name, code) in airports:
        print('The code for {0} is {1}'.format(name, code))


airports = [
    ('O’Hare International Airport', 'ORD'),
    ('Los Angeles International Airport', 'LAX'),
    ('Dallas/Fort Worth International Airport', 'DFW'),
    ('Denver International Airport', 'DEN')
]

__print__(airports)