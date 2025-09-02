# .append(item): Adds a single item to the end of the list.

# Python

# my_list = [1, 2, 3]
# my_list.append(4)  # my_list is now [1, 2, 3, 4]
# .extend(iterable): Adds all items from an iterable (like another list) to the end of the current list.

# Python

# list1 = [1, 2]
# list2 = [3, 4]
# list1.extend(list2)  # list1 is now [1, 2, 3, 4]
# .insert(index, item): Inserts an item at a specific position. The index is where the new item will be placed.

# Python

# my_list = ['a', 'c', 'd']
# my_list.insert(1, 'b')  # my_list is now ['a', 'b', 'c', 'd']
# .remove(item): Removes the first occurrence of a specified item from the list.

# Python

# my_list = ['a', 'b', 'a']
# my_list.remove('a')  # my_list is now ['b', 'a']
# .pop(index=-1): Removes an item at a given index and returns it. If no index is specified, it removes and returns the last item.

# Python

# my_list = [1, 2, 3]
# last_item = my_list.pop()   # last_item is 3, my_list is [1, 2]
# first_item = my_list.pop(0) # first_item is 1, my_list is [2]
# del statement: A general-purpose statement for removing items by index or slice. It's not a method.

# Python

# my_list = [10, 20, 30]
# del my_list[1]     # my_list is now [10, 30]
# del my_list[0:1]   # my_list is now [30]
# Other Useful Methods
# .count(item): Returns the number of times an item appears in the list.

# Python

# my_list = ['a', 'b', 'a']
# count = my_list.count('a')  # count is 2
# .index(item, start=0, end=len): Returns the index of the first occurrence of an item. A ValueError is raised if the item is not found.

# Python

# my_list = [1, 2, 3, 2]
# index = my_list.index(2)  # index is 1
# .sort(reverse=False): Sorts the list in place (modifies the original list). Use reverse=True for descending order.

# Python

# my_list = [3, 1, 2]
# my_list.sort()  # my_list is now [1, 2, 3]
# .reverse(): Reverses the order of the list in place.

# Python

# my_list = [1, 2, 3]
# my_list.reverse()  # my_list is now [3, 2, 1]
# String join() Method
# The .join() method is a powerful string method, not a list method, but it's essential for working with lists of strings.

# separator.join(list_of_strings): Concatenates all strings in an iterable with the separator string between them.

# Python

# words = ['Hello', 'World']
# sentence = " ".join(words)  # sentence is 'Hello World'

# data = ['a', 'b', 'c']
# csv_string = ",".join(data) # csv_string is 'a,b,c'





# wdym by .sort(reverse=False): Sorts the list in place (modifies the original list). Use reverse=True for descending order.


# By .sort(reverse=False), I mean that the method permanently changes the order of the original list. It doesn't create and return a new sorted list.

# Here's a breakdown of the key concepts:

# Sorts in place: This means the list is sorted "in place," which is a common term in programming. It modifies the list directly without creating a new one. The original list is permanently changed. This is an important distinction from the sorted() function, which returns a new sorted list, leaving the original unchanged.

# Python

# my_list = [3, 1, 2]
# my_list.sort() # my_list is now [1, 2, 3]

# # In contrast, the sorted() function
# original_list = [3, 1, 2]
# new_sorted_list = sorted(original_list) # new_sorted_list is [1, 2, 3]
# # original_list is still [3, 1, 2]
# reverse=False: This is an optional argument. When it's False (the default), the list is sorted in ascending order (from smallest to largest).

# reverse=True: If you want to sort the list in descending order (from largest to smallest), you can pass True to the reverse argument.

# Python

# my_list = [3, 1, 2]
# my_list.sort(reverse=True) # my_list is now [3, 2, 1]
