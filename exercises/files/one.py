'''
Create a program that opens file.txt. Read each line of the file and prepend it with a line
number.
The contents of files.txt:
This is line one.
This is line two.
Finally, we are on the third and last line of the file.
Sample output:
1: This is line one.
2: This is line two.
3: Finally, we are on the third and last line of the file.
'''

with open('./one.txt', 'r') as ones:
    for line in ones:
        print(line.rstrip())