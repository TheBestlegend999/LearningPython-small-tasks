# 1. Create a set with unique values such as:
#    Anna, Kate, Ola, Carl, Daniel, Susan
#
# 2. Add more elements to the set using the add() function:
#    Alex, Barbara, Kate, Carl, Susan, Pauline
#
# 3. Show the size of the set in the console
#
# 4. Use a loop to display all elements in the set

names = {"Anna", "Kate", "Ola", "Carl", "Daniel", "Susan"}

names.add("Alex")
names.add("Barbara")
names.add("Kate")     # duplicate, won’t be added
names.add("Carl")     # duplicate, won’t be added
names.add("Susan")    # duplicate, won’t be added
names.add("Pauline")

print("Number of elements in the set:", len(names))

for name in names:
    print(name)
