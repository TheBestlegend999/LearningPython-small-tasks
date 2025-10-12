# Assignment – Rollercoaster Ride Eligibility
#
# Use comparison and logical operators (and) to check
# if a person can ride the rollercoaster.
#
# Instructions:
# 1) Ask the user for their age and height using input().
# 2) A person must be at least 12 years old and 150 cm tall.
# 3) Use an if statement with the logical operator "and" to check both conditions.
# 4) If both conditions are met, print that the person can ride.
# 5) Otherwise, print that they do not meet the requirements.


print("Requirements for the rollercoaster ride:")
print("12 years or older and at least 150 cm tall")
print("-" * 40)

# Get user input
age = int(input("How old are you? "))
height = int(input("What is your height in cm? "))

# Check if both conditions are met
if age >= 12 and height >= 150:
    print("You can ride the rollercoaster.")
else:
    print("You do not meet the requirements.")

