import pandas as pd

std1 = {
		"Name": "test1",
		"Class": "11th A",
		"Marks_in_physics": 80,
		"Marks_in_chemistry": 85,
		"Marks_in_maths": 83
		}

std2 = {
        "Name": "test2",
        "Class": "11th B",
        "Marks_in_physics": 50,
        "Marks_in_chemistry": 55,
        "Marks_in_maths": 43
        }

std3 = {
        "Name": "test3",
        "Class": "12th A",
        "Marks_in_physics": 97,
        "Marks_in_chemistry": 95,
        "Marks_in_maths": 96
        }

std = pd.DataFrame([std1, std2, std3])

# 1st answer
print(std)

# 2nd answer
print(std.head(2))

# 3rd answer
print(std.tail(2))

# 4th answer
print(std.shape)

# 5th answer
print(len(std))

# 6th answer
print(std.values)

# 7th answer: average marks in each subject
avgphy = 0
avgchem = 0
avgmath = 0
for i in range(0, len(std)):
	avgphy += (int(std['Marks_in_physics'][i]))/(int(len(std)))
	avgchem += (int(std['Marks_in_chemistry'][i]))/(int(len(std)))
	avgmath += (int(std['Marks_in_maths'][i]))/(int(len(std)))

print(avgphy, avgchem, avgmath)


# 8th answer
total1 = int(std1['Marks_in_physics'])+int(std1['Marks_in_chemistry'])+int(std1['Marks_in_maths'])
total2 = int(std2['Marks_in_physics'])+int(std2['Marks_in_chemistry'])+int(std2['Marks_in_maths'])
total3 = int(std3['Marks_in_physics'])+int(std3['Marks_in_chemistry'])+int(std3['Marks_in_maths'])
std['Total_marks'] = total1,total2,total3


# 9th answer
percent1 = (int(std['Total_marks'][0]))/3
percent2 = (int(std['Total_marks'][1]))/3
percent3 = (int(std['Total_marks'][2]))/3

std['Percentage'] = percent1,percent2,percent3


# 10th answer
if total1 > total2 and total1 > total3:
	maxnum = total1
elif total2 > total1 and total2 > total3:
	maxnum = total2
elif total3 > total1 and total3 > total2:
	maxnum = total3
else:
	maxnum = total1 # total1 = total2 = total3

print(maxnum)


# 11th answer
print(std.index)
print(std.columns)
print(std.dtypes)
