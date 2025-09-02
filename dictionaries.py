# use curly braces
# add key-value pairs
car = {
  "brand": "Toyota",
  "model": "Camry",
  "year": 2019
}


print(car.get("model")) #Camry
print(car["model"]) #Camry



cars = {
  "car1": {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  },
  "car2": {
    "brand": "Ford",
    "model": "Focus",
    "year": 2018
  },
  "car3": {
    "brand": "Ford",
    "model": "F-150",
    "year": 2021
  }
}

# Accessing the model of 'car2'
model_of_car2 = cars["car2"]["model"]
print(model_of_car2)
# Output: Focus


cars = [
    {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    },
    {
        "brand": "Ford",
        "model": "Focus",
        "year": 2018
    },
    {
        "brand": "Ford",
        "model": "F-150",
        "year": 2021
    }
]

model_of_car1 = cars[0]["model"]
print(model_of_car1)
# Output: Mustang



# dict inside list

students = [
    {
        "id": 101,
        "name": "Alice",
        "major": "Computer Science",
        "gpa": 3.9
    },
    {
        "id": 102,
        "name": "Bob",
        "major": "Mechanical Engineering",
        "gpa": 3.2
    },
    {
        "id": 103,
        "name": "Charlie",
        "major": "Biology",
        "gpa": 3.7
    }
]

# Accessing an item from the list
print(f"The second student's name is: {students[1]['name']}")

# Iterating through all items
print("\nStudent Roster:")
for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}, Major: {student['major']}")
    
    
user_profile = {
    "username": "coder_sam",
    "email": "sam@example.com",
    "friends": ["Alice", "Bob", "Eve"],
    "preferences": {
        "theme": "dark",
        "notifications": True
    }
}

# Accessing a list within the dictionary
print(f"Sam's friends are: {user_profile['friends']}")

# Iterating through the list
print("\nSam's Friends:")
for friend in user_profile['friends']:
    print(f"- {friend}")
    
    
# set dict Value
planets = {}
planets["Earth"] = True
planets["Pluto"] = False
print(planets["Pluto"])
# Prints False

#update dict values

planets = {
    "Pluto": True,
}
planets["Pluto"] = False
print(planets["Pluto"])
# Prints False

print(planets) # {'Pluto': False}



#split
full_names = ["jack bronson", "james mcarty", "jack denver"]

names_dict = {}
for full_name in full_names:
    # .split() returns a list of strings
    # where each string is a single word from the original
    names = full_name.split()
    first_name = names[0]
    last_name = names[1]
    names_dict[first_name] = last_name

print(names_dict)


# delete

names_dict = {
    "jack": "bronson",
    "jill": "mcarty",
    "joe": "denver"
}

del names_dict["joe"]

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty'}



# True False - use key in variable - if its there -> True
cars = {
    "ford": "f150",
    "toyota": "camry"
}

print("ford" in cars)
# Prints: True

print("gmc" in cars)
# Prints: False




#ITERATING OVER A DICT

fruit_sizes = {
    "apple": "small",
    "banana": "large",
    "grape": "tiny"
}

for name in fruit_sizes:
    size = fruit_sizes[name]
    print(f"name: {name}, size: {size}")

# name: apple, size: small
# name: banana, size: large
# name: grape, size: tiny


# Complete the merge function. It accepts two dictionaries as input and returns a new merged dictionary that contains all the keys and values from the input dictionaries.


two_towers = {"Frodo": 56, "Aragorn": 10}
rotk = {"Aragorn": 100, "Gandalf": 809}
merged_dict = merge(two_towers, rotk)
print(merged_dict)
# Output: {'Frodo': 56, 'Aragorn': 100, 'Gandalf': 809}


