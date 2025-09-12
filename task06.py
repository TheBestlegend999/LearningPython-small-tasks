# 1. Create a list data with consecutive numbers: from 0 to 6
# 2. Show the length of the list in the console, delete the 2nd element
#    and show the length of the list again
# 3. Use an if conditional statement to check if the number 3 is in the list data,
#    display information in the console if this is the case. Example:
#    if 100 in someList:
#        print("100 is in the list")
# 4. Use a for loop to show the values in the list.
#    for el in someList:
#        print("list element with added value 2", el + 2)
# 5. Use a for loop to iterate through the list elements,
#    but show their values multiplied by 2



data = list(range(7))  
print("Initial list:", data)


print("Length of the list:", len(data))
del data[1]   
print("List after deleting the 2nd element:", data)
print("Length of the list after deletion:", len(data))


if 3 in data:
    print("3 is in the list")
else:
    print("3 is NOT in the list")


for el in data:
    print("List element with added value 2:", el + 2)


for el in data:
    print("List element multiplied by 2:", el * 2)
