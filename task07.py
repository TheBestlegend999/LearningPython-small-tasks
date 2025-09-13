# 1. Create a tuple with values: 50, 100, 150, 200, 250
# 2. Show the type of the tuple in the console
# 3. Show the number of elements in the tuple
# 4. Show the last element of the tuple using len() - 1
# 5. Then show the elements from the second to the fourth
# 6. Show the third element from the end using a negative index



my_tuple = (50, 100, 150, 200, 250)
print("Tuple:", my_tuple)


print("Type of my_tuple:", type(my_tuple))


print("Number of elements in tuple:", len(my_tuple))


print("Last element (using len-1):", my_tuple[len(my_tuple) - 1])


print("Elements from 2nd to 4th:", my_tuple[1:4])


print("Third element from the end:", my_tuple[-3])
