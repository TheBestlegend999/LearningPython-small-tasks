
    # Assignment – While Loop: Summing Numbers
#
# Use a while loop to add values from 0 to 100.
#
# Instructions:
# 1) Create a variable 'i' with an initial value of 0.
#    The next variable 'sum' will store the total value.
# 2) In the while loop, check if 'i' is less than or equal to 100.
#    Inside the loop, add the current value of 'i' to 'sum'.
#    Then increment 'i' by 1 in each iteration.
# 3) Add an else block that prints "End of while loop" when the loop finishes.
# 4) Print the total result as "Sum of values:" followed by the result.

#1 Initialize variables
i = 0
sum = 0

#2 While loop – add numbers from 0 to 100
while i <= 100:
    sum += i  # add current value of i to sum
    i += 1    # increment i by 1
else:
    #3 After the loop finishes
    print("End of while loop")

#4 Display the total sum
print("Sum of values:", sum)





