import pandas as pd

seriesCapCntry = pd.Series(['NewDelhi', 'WashingtonDC', 'London', 'Paris'], index=['India', 'USA', 'UK', 'France'])

# printing specific values in a series by passing known positional indices of them
print(seriesCapCntry[[2,3]])

# printing only a part of the series
print(seriesCapCntry[1:3])
# one thing to note here is, the last value is always excluded
# so if we want to print from value 1 to 3, we instead do the following than the former:
print(seriesCapCntry[1:4])

# we can also use labelled indices
print("This the capital of France:", seriesCapCntry["France"])

# to print a part of the series using labelled indices
print(seriesCapCntry['India':'France'])

# we can also apply "start, stop, step" logic here
# an application of that is to print a series in reverse order
print(seriesCapCntry[::-1])


# using series slicing to modify the values of series elements
# i.e to assign the same values to multiple elements at once
seriesCapCntry[1:4] = "Not NewDelhi"
print(seriesCapCntry)


# another key takeaway here is that when we use positional indices, the end value is always excluded. but if we use labelled indices, the end values are never excluded.
