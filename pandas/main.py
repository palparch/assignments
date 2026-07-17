import pandas as pd

series1 = pd.Series([10,20,-30,40], index=['a','b','c','d'])
series2 = pd.Series([-10,50,-50,40], index=['a','z','b','y'])

seriessum = series1.mul(series2, fill_value=0)

print("the actual number of elements in this series is ", seriessum.count())
print("and the size including the NaN values ", seriessum.size)

print(seriessum)
