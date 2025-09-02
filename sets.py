# Sets are like Lists, but they are unordered and they guarantee uniqueness. Only ONE of each value can be in a set.



fruits = {"apple", "banana", "grape"}
print(type(fruits))
# Prints: <class 'set'>

print(fruits)
# Prints: {'banana', 'grape', 'apple'}


#add value
fruits = {"apple", "banana", "grape"}
fruits.add("pear")
print(fruits)
# Prints: {'banana', 'grape', 'pear', 'apple'}


# A list with duplicate values
duplicate_fruits = ["apple", "banana", "grape", "apple", "orange", "banana"]

# Convert the list to a set to get unique values
unique_fruits_set = set(duplicate_fruits)

print(unique_fruits_set)
# Prints: {'orange', 'grape', 'banana', 'apple'}
# Note: The order of elements in a set is not guaranteed.



#remove the duplicate values
set1 = {"apple", "banana", "grape"}
set2 = {"apple", "banana"}
set3 = set1 - set2

print(set3)
# Prints: {'grape'}