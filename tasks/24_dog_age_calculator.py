
# Assignment – Dog Age to Human Age Calculator
#
# Write a program that converts a dog's age into human years.
#
# Instructions:
# 1) Ask the user to enter the dog's age and store it in a variable.
# 2) Use conditional statements to calculate the dog's age in human years.
#    - If the dog's age is 1, it equals 15 human years.
#    - For every additional year, add 9 human years.
#    Formula: human_age = 15 + (dog_age - 1) * 9
# 3) If the entered dog's age is less than or equal to 0, display an error message.
# 4) Display the result in the console.

#1 Ask for dog’s age
dog_age = float(input("Podaj wiek psa: "))

#2 Initialize human age variable
human_age = 0

#3 Conditional checks and calculations
if dog_age < 0:
    print("Wrong value. Age cannot be negative.")
elif dog_age <= 1:
    human_age = dog_age * 15
elif dog_age <= 2:
    human_age = 15 + (dog_age - 1) * 9
else:
    human_age = 24 + (dog_age - 2) * 5

#4 Display the result if valid
if dog_age > 0:
    print("Wiek psa w ludzkich latach:", human_age)


