# Assignment – Identity Operators (is, is not)
#
# Use identity operators (is, is not) to check
# the relationship between objects.
#
# Instructions:
# 1) Create a variable 'text' with value "Hello" and use the upper() method
#    to display it in uppercase. Check available methods using dir().
# 2) Create two variables 'x' and 'y' with value 256. Check if x is y.
# 3) Create a list 'listOne' with several elements. Copy 'listOne' to 'listTwo'
#    by assignment. Check if listOne is listTwo.
# 4) Modify 'listOne' by adding a new element. Check if the change affected 'listTwo'.
#    Use print to display a message about the change.
# 5) Create a new list 'listThree' with the same elements as 'listOne'.
#    Check if listOne is listThree and display the result using if.

#1 Create a string variable and use methods
text = "Hello"
print(text.upper())
print(dir(text))

#2 Check if x is y
x = 256
y = 256
print("x is y:", x is y)

#3 Create a list and assign it to another variable
listOne = [1, 2, 3]
listTwo = listOne
print("listOne is listTwo:", listOne is listTwo)

#4 Modify listOne and check if listTwo changes too
listOne.append(4)
print("After modification, listTwo:", listTwo)

if listOne is listTwo:
    print("Both variables point to the same list.")

#5 Create a new list with the same elements and compare identity
listThree = [1, 2, 3, 4]

if listOne is listThree:
    print("listOne and listThree are the same object.")
else:
    print("listOne and listThree are different objects.")



    
    
    