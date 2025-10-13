# Assignment – Blood Donation Qualification
#
# The program checks if a candidate is eligible to donate blood.
#
# Instructions:
# 1) Create variables 'age' with value 18 and 'weight' with value 50.
# 2) Write an if statement that checks if the candidate is at least 18 years old
#    and weighs at least 50 kg. If both conditions are met, print a message saying
#    they can donate blood.
# 3) If any of the conditions is not met, use else to display a message explaining why.

#1 Create variables
age = 19
weight = 55

#2 Check if both conditions are met
if age >= 18 and weight >= 50:
    print("You can donate blood.")

#3 If not eligible, explain why
else:
    if age < 18:
        print("You cannot donate blood because you are under 18.")
    elif weight < 50:
        print("You cannot donate blood because you weigh less than 50 kg.")

