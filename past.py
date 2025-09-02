num_bananas = 10
bananas = f"You have {num_bananas} bananas"
print(bananas)
# You have 10 bananas

my_mental_acuity = None
print(f"My mental acuity is {my_mental_acuity}") # None

first_name = "Lane "
last_name = "Wagner"
full_name = first_name + last_name
print(full_name)
# prints "Lane Wagner"


fruits = {"apple", "banana", "grape"}
print(type(fruits))

vegetables = ["carrot", "broccoli", "spinach"]
what_type = type(vegetables)

print(what_type)
# Prints: <class 'list'>

print(what_type.__name__)
# Prints: list


name = "Lopen"
level = 25
character_class = "Windrunner"
magic_resistance = 15.0
account_active = True

# Don't edit below this line

print("Character Report")
print(f"{name} is a level {level} {character_class}.")
print(f"They have {magic_resistance} magic resistance.")
print(f"Their account is currently active: {account_active}")

print("=========================")
print("Character Report Complete")
print("Data types:")
print(
    f"name: {type(name).__name__}, level: {type(level).__name__}, character_class: {type(character_class).__name__}"
)
print(f"magic_resistance: {type(magic_resistance).__name__}")
print(f"account_active: {type(account_active).__name__}")


# functions

def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result

area_of_circle(5) # 78.5

def subtract(a, b):
    result = a - b
    return result

def get_title(first_name, last_name, job):
    title = f"{first_name} {last_name} the {job}"
    return title


# Don't touch below this line


def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)
    print("=====================================")


test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")



#code runs top to bottom

# wont work
print(my_name)
my_name = 'Lane Wagner'
# NameError: 'my_name' is not defined

#will work
my_name = 'Lane Wagner'
print(my_name)
# Lane Wagner

---

def main():
    health = 10
    armor = 5
    add_armor(health, armor)

def add_armor(h, a):
    new_health = h + a
    print_health(new_health)

def print_health(new_health):
    print(f"The player now has {new_health} health")

# call entrypoint last
main()

---

# None return

def my_func():
    print("I do nothing")
    return None

def my_func():
    print("I do nothing")
    return

def my_func():
    print("I do nothing")


arguments vs parameters 

arguments are actual values
parameters are variable names in function definition
we can also out default values (name="Red")



# Scope
# Scope refers to where a variable or function name is available to be used. For example, when we create variables in a function (such as by giving names to our parameters), that data is not available outside of that function.


def subtract(x, y):
    return x - y
result = subtract(5, 3)

print(x) wont work
print(result)
# ERROR! "name 'x' is not defined"


global scope

pi = 3.14

def get_area_of_circle(radius):
    return pi * radius * radius

get_area_of_circle(5)


floor ZeroDivisionError
7//3 = 2 - no remainder


exponents

# 3 ** 2 

# 3 raise to the power of 2

star_rating = 4
star_rating += 1
# star_rating is now 5

star_rating = 4
star_rating -= 1
# star_rating is now 3

star_rating = 4
star_rating *= 2
# star_rating is now 8

star_rating = 4
star_rating /= 2
# star_rating is now 2.0

we cannot do ++ or -- in python, we must use += or -=

---

num = 16_000
print(num)
# Prints 16000

num = 16_000_000
print(num)
# Prints 16000000

logical operators


use. 

and or. not

print(True and True)
# prints True

print(True or False)
# prints True



---

print(not True)
# Prints: False

print(not False)
# Prints: True

# 'is not' is the preferred way to check if a variable is not None
my_variable = "Python"

if my_variable is not None:
    print("The variable has a value.")
    
    

kind alike !true in JavaScript

--

bitwise

0b0101 & 0b0111
# equals 5

binary_five = 0b0101
binary_seven = 0b0111
binary_five & binary_seven
# equals 5

0101
|
0111
=
0111

for bits of 1s and 0s

--

# Using math operators in Python is straightforward. The language uses standard symbols for common arithmetic operations.

# Basic Arithmetic Operators
# Python supports the following basic math operators:

# + (Addition): Adds two operands. 2 + 3 results in 5.

# - (Subtraction): Subtracts the right operand from the left. 5 - 2 results in 3.

# * (Multiplication): Multiplies two operands. 4 * 3 results in 12.

# / (Division): Divides the left operand by the right. This always returns a float (a number with a decimal). 10 / 2 results in 5.0.

# ** (Exponentiation): Raises the left operand to the power of the right. 2 ** 3 results in 8.

# % (Modulus): Returns the remainder of a division. 10 % 3 results in 1.

# // (Floor Division): Divides and rounds down to the nearest whole number (an integer). 10 // 3 results in 3.


---

5 < 6 # evaluates to True
5 > 6 # evaluates to False
5 >= 6 # evaluates to False
5 <= 6 # evaluates to True
5 == 6 # evaluates to False
5 != 6 # evaluates to True

same as js but without ===
double only not triple

--


is_bigger = 5 > 4
is_bigger = True

print(is_bigger)  #true

---



