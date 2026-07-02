import pandas as pd
import csv

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

    return str(finalint)


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
    classtocheck = 'Classname:' + str(input("From which class? :"))
    counter = 0
    print(classtocheck)


    with open('students.csv', 'r') as f:
        mycsv = csv.reader(f)
        csvlist = list(mycsv)

        classlist = []

        for row in csvlist:
            if str(row[2]) == classtocheck:
                classlist.append(csvlist[counter])
                counter+=1
                    #print(csvlist[counter])
            else:
                counter+=1        


        marks_of_all = []
        for student in classlist:
            ineng = wordstoint(student[4])
            inphy = wordstoint(student[5])
            inchem = wordstoint(student[6])
            inmaths = wordstoint(student[7])
            inip = wordstoint(student[8])

            marks_of_all.append(int(ineng) + int(inphy) + int(inchem) + int(inmaths) + int(inip))

        max_marks, topper_index = findmaxandindex(marks_of_all)

        print(classlist[topper_index])

def subavgmarks():
    with open('students.csv', 'r') as f:
        mycsv = csv.reader(f)
        csvlist = list(mycsv)

        alleng = []
        allphy = []
        allchem = []
        allmaths = []
        allip = []

        for row in csvlist:
            alleng.append(wordstoint(row[4]))
            allphy.append(wordstoint(row[5]))
            allchem.append(wordstoint(row[6]))
            allmaths.append(wordstoint(row[7]))
            allip.append(wordstoint(row[8]))

        avgeng, avgphy, avgchem, avgmaths, avgip = [], [], [], [], []

        totale, totalp, totalc, totalm, totali = 0, 0, 0, 0, 0
        for marks in alleng:
            totale+=int(marks)
        avgeng = totale/(len(alleng))
        
        for marks in allphy:
            totalp+=int(marks)
        avgphy = totalp/(len(allphy))

        for marks in allchem:
            totalc+=int(marks)
        avgchem = totalc/(len(allchem))

        for marks in allmaths:
            totalm+=int(marks)
        avgmaths = totalm/(len(allmaths))

        for marks in allip:
            totali+=int(marks)
        avgip = totali/(len(allip))
        

        print("\n")
        print("----------------------")

        print("Average in English: ", avgeng)
        print("Average in Physics: ", avgphy)
        print("Average in Chemistry: ", avgchem)
        print("Average in Maths: ", avgmaths)
        print("Average in IP: ", avgip)
            
def exportsummary():
    
            
            
# print menu
print("Select an option:")
print("1. Enter new student data")
print("2. Display all records")
print("3. Search a student by roll number")
print("4. Display topper of the class")
print("5. Display subject-wise average marks")
print("6. Export a summary of the records to a CSV file")


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
