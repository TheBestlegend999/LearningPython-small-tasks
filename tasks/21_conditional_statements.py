# Assignment – Conditional Statements (if, elif, else)
#
# Use conditional statements to create a simple decision program
# that analyzes the value of a variable called 'number'.
#
# Instructions:
# 1) Create a variable 'number' and assign it the value 15.
# 2) Check if 'number' is greater than 10. If true, display a message.
# 3) Check if 'number' is equal to 15. If true, display a message.
# 4) Use 'elif' to check if 'number' equals 20, 25, or is greater than 30.
#    Display a message for each case.
# 5) If none of the above conditions are met, use 'else' to display a default message.
# 6) Add a nested conditional inside one of the cases to check an additional condition.

#1 Create the variable
number = 15

#2 Check: number > 10
if number > 10:
    print("The number is greater than 10.")

#3 Check: number == 15 (independent check)
if number == 15:
    print("The number is exactly 15.")

#4 Use an if/elif chain for other cases
if number == 20:
    print("The number is 20.")
elif number == 25:
    print("The number is 25.")
elif number > 30:
    print("The number is greater than 30.")
#5 Default message for the chain above
else:
    print("No match in the 20/25/>30 checks.")

#6 Nested condition inside a case (extra check when number > 10)
if number > 10:
    if number > 50:
        print("Nested: the number is also greater than 50.")
    else:
        print("Nested: the number is not greater than 50.")



