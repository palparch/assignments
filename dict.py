# lets learn how to use dictionaries, as i never properly learned how to use one.

import pandas as pd


dict1 = {
        "name": "palparch",
        "skills": "python programming at a mediocre level",
        "date": "19 july 2026",
        "bad data": "idk man"
        }


print(dict1)

# lets try retrieving data
print("the name of the person is:", dict1["name"])

# lets try removing a value 
del dict1["bad data"]
print(dict1)

# lets iterate over one
print(dict1.items())
for key, value in dict1.items():
    print("this is the key,", key)
    print("this is the value,", value)

# okay so finally, lets try converting one into a pandas series
dictseries = pd.Series(dict1)
print("this is the dictionary as a pandas series")
print(dictseries)

# as a final task, lets try asking the user for key and value pairs to make a custom dictionary and then print it
userdict = {}

numofitems = int(input("How many key value pairs do you want? "))

for i in range(0, numofitems):
    userkey = input("Enter the key: ")
    uservalue = input("Enter the value: ")

    userdict[userkey] = uservalue

print("This is the formed dictionary")
print(userdict)
