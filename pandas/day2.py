import pandas as pd


# making the dataframe first
std1 = pd.Series(['Rahul', 9, 1, 80, 90, 60], 
				 index=['Name', 'Class', 'Roll Number', 'Marks in Physics', 'Marks in Chemistry', 'Marks in Maths'])
std2 = pd.Series(['Priya', 10, 2, 88, 85, 92],
                 index=std1.index)
std3 = pd.Series(['Aman', 12, 3, 76, 81, 79],
                 index=std1.index)
std4 = pd.Series(['Sneha', 12, 4, 95, 93, 97],
                 index=std1.index)
std5 = pd.Series(['Rohan', 11, 5, 69, 74, 71],
                 index=std1.index)
std6 = pd.Series(['Ananya', 11, 6, 91, 89, 94],
                 index=std1.index)
std7 = pd.Series(['Karan', 12, 7, 83, 78, 80],
                 index=std1.index)
std8 = pd.Series(['Meera', 9, 8, 87, 90, 86],
                 index=std1.index)
std9 = pd.Series(['Arjun', 11, 9, 72, 68, 75],
                 index=std1.index)
std10 = pd.Series(['Neha', 10, 10, 98, 96, 99],
                  index=std1.index)


df = pd.DataFrame([std1,std2,std3,std4,std5,std6,std7,std8,std9,std10])


# task 1
print(df)
print(df.index) # row labels, but why is it numeric?
print(df.columns) # column labels, they are correct
print(df.dtypes) # data types, correct
print(df.shape) # dimension, correct


# task 2
# printing only student names with their Maths marks
print(df['Marks in Maths']) # prints only marks in maths

# printing only students from a particular class, idk how to sorry
# the only thing i know is this:
print(df['Class']==12) # but this doesnt print all the records sadly
# and i tried using loops to but i just cant think about it at all
# but if i really try:
values = (df['Class']==12).values
print("Students in class 12:")
for i in range(0, len(values)):
	if values[i]:
		print((df.values)[i])
# i know i could have done it better using loops only but i could only think about this for now

# printing only students scoring above 80 in Physics
values = (df['Marks in Physics']>80).values
print("Students that scored more than 80 in physics:")
for i in range(0, len(values)):
    if values[i]:
        print((df.values)[i])


# task 3
print(df.loc[2, :]) # 3rd student
print(df.loc[5, :]) # 6rd student
print(df.loc[8, :]) # 9rd student

# printing marks of chemistry of all students:
print(df.loc[:, 'Marks in Chemistry'])


# task 4
# changing marks of say, Ananya
df.loc[5] = [df.loc[5, 'Name'], df.loc[5, 'Class'], df.loc[5, 'Roll Number'], 40, 34, 55]

# adding a column contaning total marks
for i in range(0, len(df)):
	df.loc[i, 'Total Marks'] = int(df.loc[i, 'Marks in Physics']) + int(df.loc[i, 'Marks in Chemistry']) + int(df.loc[i, 'Marks in Maths'])

# adding a new column containing total percentage
for i in range(0, len(df)):
	df.loc[i, 'Percentage'] = round((int(df.loc[i, 'Total Marks'])/3), 2)


# task 5
for i in range(0, len(df)):
	if int(df.loc[i, 'Percentage']) >= 40: # ahh sad, everyone passed in this school
	    df.loc[i, 'Result'] = "Pass"
	else:
		df.loc[i, 'Result'] = "Fail"



# task 6
# delete one student record
df = df.drop(1, axis=0)

# delete one unnecessary column, i think total marks is kinda unnecessary
df = df.drop('Total Marks', axis=1)



# task 7
# add a new student record
df.loc[len(df)] = ['Karnika', 8, 11, 100, 100, 100, 100, 'Pass']
# add a new column containing some calculated information, i already did that im skipping that


# task 8
df.to_csv(path_or_buf='students.csv', index=False)



# task 9
newdf = pd.read_csv('students.csv', sep=',', header=0)


df = df.drop('Total Marks', axis=1)



# task 7
# add a new student record
df.loc[len(df)] = ['Karnika', 8, 11, 100, 100, 100, 100, 'Pass']
# add a new column containing some calculated information, i already did that im skipping that


# task 8
df.to_csv(path_or_buf='students.csv', index=False)



# task 9
newdf = pd.read_csv('students.csv', sep=',', header=0)
