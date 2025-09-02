



if

elif

else

score = 20
high_score = 100
second_highest_score = 80
third_highest_score = 70

if score > high_score:
    print("High score beat!")
elif score > second_highest_score:
    print("You got second place!")
elif score > third_highest_score:
    print("You got third place!")
else:
    print("Better luck next time")
    
    

def is_dog(num_legs, weight):
    return num_legs == 4 and weight < 100

#return 2 things
--

def is_dog(num_legs, weight):
    return num_legs == 4 and weight < 100


def is_cat(num_legs, weight):
    return num_legs == 4 and weight >= 100


--

#LOOPS

for i in range(0, 10):
    print(i)

    
    #34d params is step
for i in range(0, 10, 2):
    print(i)
# prints:
# 0
# 2
# 4
# 6
# 8

#backwards

for i in range(3, 0, -1):
    print(i)
# prints:
# 3
# 2
# 1

def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total

sum_of_numbers(1, 5)  # returns 10 (1+2+3+4+5)

# Yes, you're correct. The number 5 was not included in the sum.

# This is because the Python range(start, end) function is exclusive of the end value. It starts at start and goes up to, but does not include, end. In your code, range(1, 5) generates the numbers 1, 2, 3, and 4.


def countdown_to_start():
    for i in range(10, 0, -1):
        print(f"{i}...")

    print(f"{i}... Fight!")

countdown_to_start()


# 10...
# 9...
# 8...
# 7...
# 6...
# 5...
# 4...
# 3...
# 2...
# 1...
# 1... Fight!



# convert to list

my_range = range(5)
my_list = list(my_range)



strings = ["apple", "banana", "cherry"]

for index, value in enumerate(strings):
    print(f"Index {index}: {value}")
# Output:
# Index 0: apple
# Index 1: banana
# Index 2: cherry