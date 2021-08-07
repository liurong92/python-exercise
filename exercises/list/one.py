'''
Create a Python program that captures and displays a person's to­do list. Continually prompt
the user for another item until they enter a blank item. After all the items are entered, display the
to­do list back to the user.
Sample Output:
Enter a task for your to­do list. Press <enter> when done: Buy cat
food.
Task added.
Enter a task for your to­do list. Press <enter> when done: Mow the
lawn.
Task added.
Enter a task for your to­do list. Press <enter> when done: Take
over the world.
Task added.
Enter a task for your to­do list. Press <enter> when done:
Your To­Do List:
Buy cat food.
Mow the lawn.
Take over the world.
'''

todo_list = []
is_finish = False

while not is_finish:
    custom_todo = input('Enter a task for your todo list. Press <enter> when done: ')
    if len(custom_todo) != 0:
        todo_list.append(custom_todo)
        print('Task added')
    else:
        is_finish = True

print('\nYour todo List:\n{}'.format('-' * 16))
for todo in todo_list:
    print(todo)

