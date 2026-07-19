import pandas as pd

# lets learn how to add, sub, mul, div two series
# there are two ways to do so
# 1. using normal operators
# 2. using explicit method call 
# we will only use the explicit method call way of operating on series here to keep things simple 

series1 = pd.Series([10,15,20,30,40], index=['a','b','c','d','e'])
series2 = pd.Series([1,2,3,0,5], index=['a','x','b','d','y'])


# adding them
print(series1.add(series2, fill_value=0))

# subtracting them
print(series1.sub(series2, fill_value=0))

# multiplying them
print(series1.mul(series2, fill_value=0))

# okay this is going to be interesting
# we got some zero values as denominators here, so lets see what that returns
# dividing them
print(series1.div(series2, fill_value=0)) 
# as a result, we get "inf" for the values where we divide any number by zero. 



# just a random thing i wanted to check
#if (series1 + series2) == (series1.add(series2, fill_value=0)):
#    print("yeah they are the same")
# ah okay that didnt work, nvm
