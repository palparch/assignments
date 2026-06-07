import pandas as pd

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

studentseries = pd.Series([name, rollno, classname, section, markse, marksp, marksc, marksm, marksip],
                          index = ['Name', 'RollNo', 'Classname', 'Section', 'Marks in English', 'Marks in Physics', 'Marks in Chemistry', 'Marks in Maths', 'Marks in IP'])


with open("students.csv", "a") as file:
    file.write(data_list)
