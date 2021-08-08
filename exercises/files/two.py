'''
Read the contents of animals.txt and produce a file named animals­sorted.txt that is sorted
alphabetically.
The contents of animals.txt:
man
bear
pig
cow
duck
horse
dog

After the program is executed the contents of animals­sorted.txt should be:
bear
cow
dog
duck
horse
man
pig
'''

animals = []

with open('./animals.txt') as animals_file:
    for line in animals_file:
        animals.append(line)
animals.sort()

try:
    with open('./animals-sorted.txt', 'w') as animals_sorted_file:
        for animal in animals:
            animals_sorted_file.write(animal)
except:
    print('error')