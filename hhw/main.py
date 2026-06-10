import pandas as pd
import csv

# print menu
print("Select an option:")
print("1. Enter new student data")
print("2. Display all records")
print("3. Search a student by roll number")
print("4. Display topper of the class")
print("5. Display subject-wise average marks")

def findmaxandindex(givenlist):
    modiflist = []
    modiflist[:] = givenlist[:]
    for i in range(0, len(modiflist)):
        for j in range(0, len(modiflist)):
            if modiflist[i] > modiflist[j]:
                modiflist[i],modiflist[j] = modiflist[j],modiflist[i]
    
    maxnum = modiflist[0]

    counter = -1
    for num in givenlist:
        counter+=1
        if num == maxnum:
            break
    
    return maxnum, counter



def wordstoint(givenlist):
    intwordlist = []
    wordlist = []
    for i in givenlist:
        wordlist.append(i)

    for i in range(0, len(wordlist)):
        try:
            testvar = int(wordlist[i])
            intwordlist.append(testvar)
        except:
            continue

    finalint = ""

    for i in range(0, len(intwordlist)):
        finalint+=str(intwordlist[i])

    return int(finalint)


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
                          index = ['Name', 'RollNo', 'Classname', 'Section', 'MarksinEnglish', 'MarksinPhysics', 'MarksinChemistry', 'MarksinMaths', 'MarksinIP'])


    with open("students.csv", "a") as file:
        for i, v in studentseries.items():
            entry = str(i) + ":" + str(v) + ","
            file.write(entry)
        file.write("\n")

#def loadcsvtopandas():
    

def displayrecords():
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
        csvlist = list(mycsv)
        rolltocheck = 'RollNo:' + str(reqrollno)
        counter = 0
        
        for row in csvlist:
            if str(row[1]) == rolltocheck:
                print("Roll number successfully found.")
                break
                #print(csvlist[counter])
            else:
                counter+=1
        print(csvlist[counter])



def displaytopper():
    with open('students.csv', 'r') as f:
        mycsv = csv.reader(f)
        csvlist = list(mycsv)
        counter = 0
    
        marksineng = []
        marksinphy = []
        marksinchem = []
        marksinmaths = []
        marksinip = []

        for row in csvlist:
            marksineng.append(wordstoint(row[4]))
            marksinphy.append(wordstoint(row[5]))
            marksinchem.append(wordstoint(row[6]))
            marksinmaths.append(wordstoint(row[7]))
            marksinip.append(wordstoint(row[8]))

        markslist = []
        for i in range(0, len(marksineng)):
            totalmarks = int(str(marksineng[i]+marksinphy[i]+marksinchem[i]+marksinmaths[i]+marksinip[i]))
            markslist.append(totalmarks)
        
        print("max marks: ", findmaxandindex(markslist[:]))
        maxmarks, topperindex = findmaxandindex(markslist[:])

        print(csvlist[topperindex])

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
    #print(wordstoint('MarksinEnglish:81'))
elif user_input == 5:
    subavgmarks()
else:
    print("This is not a valid option. Please enter a valid option.")
