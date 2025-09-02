# Assignment
# Complete the number_sum function. It should add up all the numbers from 1 to n and return the result. For example:

# number_sum(5) -> 1+2+3+4+5 -> 15
# number_sum(3) -> 1+2+3 -> 6

# def sum_number(n):
#     total = 0
#     for i in range(1, n + 1):
#         total+= i
#     return total

# print(sum_number(3))
# print(sum_number(5))


# Find Min
# In this problem you'll need a way to represent the largest possible number: infinity. In Python, you can use this constant to represent positive infinity:

# my_infinity = float("inf")

# Assignment
# Write a function called find_min() that finds the smallest number in a list. For example:

# find_min([1, 3, -1, 2]) -> -1
# find_min([18, 3, 7, 2]) -> 2


#indentation - if its almost after and not indent - python will see as part of the expression
# def find_min(list):
#     min_value = float("inf")
#     for num in list:
#         if num < min_value:
#             min_value = num
#     return min_value


# print(find_min([1, 3, -1, 2]))
# print(find_min([18, 3, 7, 2]))
#
#
#
# Assignment
# Complete the remove_nonints() function.
# It takes a list and returns a new list but with all the non-integer types removed.
#
#
# def remove_nonints(list):
#     new_list = []
#     for item in list:
#         if isinstance(item, int):
#             new_list.append(item)
#     return new_list

# new_list = remove_nonints(["1", 1, "3", "400", 4, 500])
# print(new_list)
# # [1, 4, 500]



#useful methods
#
#


FOR RANGE - access index
FOR NUM IN NUMBERS - access value
FOR INDEX, VALUE enumerate(list)- access both index and value