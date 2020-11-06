# Tasks
import random


# Make a range with a loop that says hello 10 times
for _ in range (10):
    print('Hello!')

# create another loop with a range that asks for names and appends to list_names
list_names = []
list_size = 3

for _ in range (list_size):
    list_names.append(input('What is your name?'))

print(list_names)

# make a loop that iterates over each name in list_namess and formats it to lower case in a new variable list_names_lower
list_names_lower = []
for _ in list_names:
    list_names_lower.append(_.lower())


print(list_names_lower)
# find if the list of names has an even number of items 

if len(list_names) % 2 == 0:
    print('This list contains an even number of items.')
else:
    print('This list contains an odd number of items.')