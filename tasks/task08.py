# 1. Create a variable config which will be a dictionary
# with website configuration, save the following keys with values:
# - "website" with value "example.com"
# - "dbType" with value "mysql"
# - "dbUser" with value "admin"
# - "dbPassword" with value "12345"
#
# 2. Show the number of elements in the dictionary in the console
#
# 3. Show in the console the value of the key "dbType" from the dictionary
#
# 4. Use a for loop to iterate over all dictionary elements
# and display them in the console in the format:
# "Key in config: website with value example.com"


config = {
    "website": "example.com",
    "dbType" : "mysql",
    "dbUser" : "admin",
    "dbPassword" : 12345,
}

print("Number of elements: ", len(config))
print (config["dbType"])

for key, value in config.items():
    print ("Key in config: ", key, "with value: ", value)