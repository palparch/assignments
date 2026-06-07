# accepts student data

name = input("Enter the student's name: ")
rollno = int(input("Enter the roll number: "))
classname = int(input("Enter the class: "))
section = input("Enter the section: ")
print("Now please enter the marks of the individual subjects.")
markse = int(input("Marks in English: "))
marksp = int(input("Marks in Physics: "))
marksc = int(input("Marks in Chemistry: "))
marksm = int(input("Marks in Maths: "))
marksip = int(input("Marks in IP: "))

for i in range(0, 11):
    data_list.append()

data_list = []
data_list.append(name, rollno, classname, section, markse, marksp, marksc, marksm, marksip)

with open("students.csv", "a") as file:
    file.write(data_list)
