# Assignment – Candidate Qualification Check
#
# Write a program that checks if a potential candidate
# meets the requirements for a programming position.
#
# Instructions:
# 1) Create a variable 'experience' with the value 2, and a list called 'languages'
#    containing: ['python', 'javascript', 'java']. The last variable should be 'contractType'
#    with the value 'b2b'.
# 2) Use if statements and the 'in' operator to check if the candidate
#    knows the 'python' language and if 'experience' is greater than or equal to 1.
#    If both conditions are true, print that the candidate meets the technical requirements.
# 3) Use another if statement with the 'or' operator to check if the candidate
#    knows 'python' or 'java'. If so, print that the candidate fits the job requirements.
# 4) If any of the conditions are not met, use 'else' to print an appropriate message.


experience = 2
languages = ["python", "typescript", "javascript", "java"]
contractType = "b2b"

#2 Check if candidate knows Python and has experience
if experience >= 1 and "python" in languages:
    print("Employee meets basic technical requirements.")

    #3 Nested check – verify contract type or additional language
    if contractType == "b2b" or "java" in languages:
        print("Employee meets all requirements for employment.")
    else:
        print("Employee does not meet all hiring conditions.")

#4 If the first condition is not met
else:
    print("Employee does not meet basic requirements.")


