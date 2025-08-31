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

