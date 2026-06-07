import pandas as pd
import csv

print("Select an option:")
print("1. Enter new student data")
print("2. Display all records")
print("3. Search a student by roll number")
print("4. Display topper of the class")
print("5. Display subject-wise average marks")

def enterstddata():
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
        for i, v in studentseries.items():
            entry = str(i) + ":" + str(v) + ","
            file.write(entry)
            file.write(" ")
        file.write("\n")


def displayrecords(rollindex):
    with open('students.csv', 'r') as f:
        mycsv = csv.reader(f)
        for row in mycsv:
            i = 0
            print("\n")
            while i != 9:
                print(row[i])
                i+=1


def searchstdbyrollno(reqrollno):
    with open('students.csv', 'r') as f:
        mycsv = csv.reader(f)
        rollnolist = []
        for row in mycsv:
            rollnolist.append(row[1]) 
        modifrollno = ' RollNo:' + str(reqrollno)
        #print(modifrollno)
        for rno in rollnolist:
            if rno == modifrollno:
                rnindex = rollnolist.index(rno)
            #print(rnindex)
            #print(row[:])
            print(row[])

def displaytopper():
    print("WIP nga")

def subavgmarks():
    print("WIP nga")
    
    
    
user_input = int(input("What do you want to do? Enter the number corresponding to the function you want to do: "))

if user_input == 1:
    enterstddata()
elif user_input == 2:
    displayrecords()
elif user_input == 3:
    reqrollno = int(input("Which roll no.: "))
    searchstdbyrollno(reqrollno)
elif user_input == 4:
    displaytopper()
elif user_input == 5:
    subavgmarks()
else:
    print("This is not a valid option. Please enter a valid option.")
