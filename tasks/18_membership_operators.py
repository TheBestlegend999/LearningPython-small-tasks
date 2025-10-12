# Assignment – Membership Operators (in, not in)
#
# Use membership operators (in, not in) to check
# the presence of elements in collections and apply
# conditional statements (if) to display messages.
#
# Instructions:
# 1) Check if the number 7 is in the list 'numbers' and print the appropriate message.
# 2) Check if the word 'cat' is not in the tuple 'animals' and print the appropriate message.
# 3) Create a dictionary 'user' with keys 'name' and 'age'.
#    Check if the key 'name' exists in the dictionary and print the result.


#1 Check if number 7 is in the list
numbers = [1, 3, 5, 7, 9]

if 7 in numbers:
    print("7 is in the list.")
else:
    print("7 is not in the list.")

#2 Check if 'cat' is not in the tuple
animals = ("dog", "bird", "fish")

if "cat" not in animals:
    print("'cat' is not in the tuple.")
else:
    print("'cat' is in the tuple.")

#3 Check if key 'name' exists in dictionary
user = {"name": "Arthur", "age": 44}

if "name" in user:
    print("Key 'name' exists in the dictionary.")
else:
    print("Key 'name' does not exist in the dictionary.")


 