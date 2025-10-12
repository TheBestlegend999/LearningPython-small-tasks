# Assignment – operations on a bank account.
# Use augmented assignment operators with a math operation, e.g.: +=  -=  *=  /=  etc.
# Note: after each operation, print the balance to the console.

# 1) Create a variable balance with the initial value 1000.
# 2) Add the amount of a new salary: 7000.
# 3) Subtract 2000 for the apartment.
# 4) A bank error tripled your balance.
# 5) Subtract 4000 for a computer.
# 6) The bank noticed the mistake and reverses the last transaction.
#    Add 4000 to the balance, divide it by 3, and only then subtract 4000.
# 7) Show the final balance.




# 1) 
balance = 1000
print("Initial balance:", balance)

# 2) 
balance += 7000
print("After adding salary:", balance)

# 3)
balance -= 2000
print("After paying for apartment:", balance)

# 4) 
balance *= 3
print("After bank error (tripled):", balance)

# 5) Subtract 4000 for a computer.
balance -= 4000
print("After buying a computer:", balance)

# 6) The bank noticed the mistake and reverses the last transaction.
#    Add 4000 to the balance, divide it by 3, and only then subtract 4000.
balance += 4000
balance /= 3
balance -= 4000
print("After bank correction:", balance)

# 7) Show the final balance.
print("Final balance:", balance)

