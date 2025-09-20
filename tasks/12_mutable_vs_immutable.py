# 1. Task to complete:

# 1. Declare a variable 'number' as an int with value 5 and print its memory address.
# 2. Increase 'number' by 2 and print its memory address again.
# 3. Create a list 'fruits' with three items: "apple", "banana", "cherry".
#    Print the memory address of the list.
# 4. Append another fruit "orange" to 'fruits' and print the list's memory address.
# 5. Based on the actions above, explain the difference between mutable and immutable types:
#    - Immutable types (e.g., int, str, tuple): operations create a NEW object -> the id() usually changes.
#    - Mutable types (e.g., list, dict, set): you can change the object IN PLACE -> the id() stays the same.




number = 5
print("number:", number, "id:", id(number))

number += 2
print("number after += 2:", number, "id:", id(number))

fruits = ["apple", "banana", "cherry"]
print("fruits:", fruits, "id:", id(fruits))

fruits.append("orange")
print("fruits after append:", fruits, "id:", id(fruits))



