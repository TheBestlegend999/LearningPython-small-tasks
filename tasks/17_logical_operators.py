# Assignment – Logical Operators (and, or, not)
#
# Use logical operators to check different conditions
# and display appropriate messages in the console.
#
# Instructions:
# 1) Check if 'hoursWorked' > 8 and 'projectFinished' == True.
#    If both are true, print "You can go home."
# 2) Check if temperature 'temp' < 0 or > 30.
#    If true, print "Extreme weather conditions."
# 3) Use 'not' to check if 'isHoliday' == False.
#    If true, print "Today is a working day."
# 4) Using any combination of operators, check if:
#    'errorsFound' < 10 and 'warnings' == 0.
#    If true, print "Code looks good."
#    Otherwise, print "Check your code again."


#1 Check if 'hoursWorked' > 8 and 'projectFinished' is True
hoursWorked = 9
projectFinished = True

if hoursWorked > 8 and projectFinished:
    print("You can go home.")

#2 Check if temperature is below 0 or above 30
temp = 35

if temp < 0 or temp > 30:
    print("Extreme weather conditions.")

#3 Use 'not' to check if today is not a holiday
isHoliday = False

if not isHoliday:
    print("Today is a working day.")

#4 Check if 'errorsFound' < 10 and 'warnings' == 0
errorsFound = 12
warnings = 1

if errorsFound < 10 and warnings == 0:
    print("Code looks good.")
else:
    print("Check your code again.")


    

    
