'''
Create a program that asks the user how far they want to travel. If they want to travel less than
three miles tell them to walk. If they want to travel more than three miles, but less than three
hundred miles, tell them to drive. If they want to travel three hundred miles or more tell them to
fly.
Sample Output:
How far would you like to travel in miles? 2500
I suggest flying to your destination.
'''

custom_input = input('How far would you like to travel in miles?')
distance = int(custom_input)

if distance <= 3:
    transport = 'walking'
elif distance < 300:
    transport = 'driving'
else:
    transport = 'flying'

print('I suggest {} to your destination.'.format(transport))
