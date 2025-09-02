names = ["Bob", "Lane", "Alice", "Breanna"]

for i in range(len(names)):
    print(f"Index {i} contains {names[i]}")


# methods

#len, acces[0], append(), remove()

for name in names:
    print(name)

cards = []
cards.append("nvidia")
cards.append("amd")

print(cards)  # the cards list is now ['nvidia', 'amd']

cards = []
cards.append("nvidia")
cards.append("amd")

print(cards)  # the cards list is now ['nvidia', 'amd']


cards = ["nvidia", "amd"]

cards.append("ewan")

print(cards)

# appends adds at the end

.pop() is the opposite of .append(). Pop removes the last element from a list and returns it for use. For example:

vegetables = ["broccoli", "cabbage", "kale", "tomato"]
last_vegetable = vegetables.pop()
# vegetables = ['broccoli', 'cabbage', 'kale']
# last_vegetable = 'tomato'

#pop removes last element

#count items ina list

sports = ["soccer", "basketball", "baseball"]

count = len(sports)

print(f"I play {count} sports")

#directly access the value

trees = ['oak', 'pine', 'maple']
for tree in trees:
    print(tree)
# Prints:
# oak
# pine
# maple

#find item in a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        print("Found a banana!")
        


#infinity

positive_infinity = float('inf')
negative_infinity = float('-inf')

import math
another_positive_infinity = math.inf



#empty lisr/dict

# Using square brackets (most common)
empty_list = []

# Using curly braces (most common)
empty_dict = {}

#find max value

numbers = [100, 10, 22]
max_val = max(numbers)
print(max_val)  # Output: 100



#modulo
remainder = 8 % 3
# remainder = 2


#slicing lists

my_list[ start : stop : step ]

scores = [50, 70, 30, 20, 90, 10, 50]
# Display list
print(scores[1:5:2])
# Prints [70, 20]


#concantenating lists
total = [1, 2, 3] + [4, 5, 6]
print(total)
# Prints: [1, 2, 3, 4, 5, 6]


fruits = ["apple", "orange", "banana"]
print("banana" in fruits)
# Prints: True

fruits = ["apple", "orange", "banana"]
print("banana" not in fruits)
# Prints: False


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# delete the fourth item
del nums[3]
print(nums)
# Output: [1, 2, 3, 5, 6, 7, 8, 9]

# delete the second item up to (but not including) the fourth item
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[1:3]
print(nums)
# Output: [1, 4, 5, 6, 7, 8, 9]

# delete all elements
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[:]
print(nums)
# Output: []# delete the entire list


#TUPLES - ()

my_tuple = ("this is a tuple", 45, True)
print(my_tuple[0])
# this is a tuple
print(my_tuple[1])
# 45
print(my_tuple[2])
# True


# Tuple Unpacking
# You can easily assign the values of a tuple to variables using unpacking.

dog = ("Fido", 4)
dog_name, dog_age = dog
print(dog_name)
# Fido
print(dog_age)
# 4



#reverse list
the_names = ("Alice", "Bob", "Charlie")

for i in range(len(the_names), 0, -1):
    print(the_names[i - 1]) #starts from the last element