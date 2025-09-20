# Task to do:

# 1. Create a list 'numbers' containing numbers from 7 to 12.
#    Display this list.

# 2. Convert the list 'numbers' into a tuple 'tupleNumbers'
#    and display the result.

# 3. Create a list 'mixedList' consisting of different data types,
#    e.g., string, integer, floating-point number.
#    Display 'mixedList'.

# 4. Transform 'mixedList' into a set 'setMixed'
#    and display its type and contents.

# 5. Convert 'tupleNumbers' into a frozen set 'frozenSetNumbers'
#    and display its type and contents.

# 6. Create a tuple 'nameAgePairs' containing pairs (name, age),
#    and then based on it create a dictionary 'ageDict'.
#    Display the dictionary, and then display the age of the person named 'Marek'.


numbers = list(range(7, 13))
print("numbers:", numbers)

tupleNumbers = tuple(numbers)
print("tupleNumbers:", tupleNumbers)

mixedList = ["hello", 42, 3.14] 
print("mixedList:", mixedList)

setMixed = set(mixedList)
print("setMixed (type):", type(setMixed))
print("setMixed (contents):", setMixed)

frozenSetNumbers = frozenset(tupleNumbers)
print("frozenSetNumbers (type):", type(frozenSetNumbers))
print("frozenSetNumbers (contents):", frozenSetNumbers)

nameAgePairs = (("Marek", 22), ("Ola", 19), ("Adam", 30))
ageDict = dict(nameAgePairs)
print("ageDict:", ageDict)
print("Marek's age:", ageDict.get("Marek", "not found"))
