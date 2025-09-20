# Task to complete:

# 1. Create a variable decimalNum with the decimal value 45.6789
# 2. Convert decimalNum to an integer (int) and save the result
#    in the variable wholeNum. Display the type of the variable wholeNum and its value.
# 3. Transform the string "4321" into an integer and display the type after conversion.
# 4. Create a variable wholeNum2 with the integer value 123, then convert
#    it to a floating-point number (float) and display its type and value.
# 5. Convert the string "98.76" into a floating-point number and display
#    its type and value.
# 6. Use the print function to display a text string containing
#    the value of wholeNum2, combining it with text and other data types (e.g.,
#    a floating-point value, a list). Use two methods: concatenation
#    with the str() function and separating values with commas in the print function.

decimalNum = 45.6789

wholeNum = int(decimalNum)
print("wholeNum:", wholeNum, "| type:", type(wholeNum))

num_from_string = int("4321")
print("num_from_string:", num_from_string, "| type:", type(num_from_string))

wholeNum2 = 123
floatNum2 = float(wholeNum2)
print("floatNum2:", floatNum2, "| type:", type(floatNum2))

float_from_string = float("98.76")
print("float_from_string:", float_from_string, "| type:", type(float_from_string))

print("The value of wholeNum2 is " + str(wholeNum2) + " and here is a list: " + str([1, 2, 3]))

print("The value of wholeNum2 is", wholeNum2, "and here is a list:", [1, 2, 3])


