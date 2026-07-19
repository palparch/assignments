# lets learn about the attributes in pandas, basic ones
# the mnemonic to remember, VEINS

import pandas as pd

# lets define a sample series first
days = pd.Series([31,28,31,30,31,30,31,31,30,31,30,31], index=['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# VALUES
# used to print all the values in a series
print(days.values)

# EMPTY
# tells us whether a series is empty or not
print(days.empty) # it should print False

# INDEX.NAME
# used to assign a name to the index column
days.index.name = "Month"

# NAME
# used to assign a name to the whole series
days.name = "Number of days in a month"
print(days)

# size
# used to print the size of a series
# this is different from using ".count()", because this also includes all the "NaN" values while ".count()" doesnt
print("Number of months in a year is:", days.size)
