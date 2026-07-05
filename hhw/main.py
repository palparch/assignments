import pandas as pd
import math
import csv

linelen = 34

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



def countword(word):
    wordlist = list(word)
    wordcount = 0
    for entity in word:
        wordcount += 1
    return int(wordcount)



def cleanprint(listtoprint, title):
    wordcount = int(countword(title))


    print("+--------------------------------+")
    print("|", end='')
    print(" "*(math.floor((int(linelen-wordcount))/2)-1), end='')
    print(title, end='')

    if wordcount % 2 == 0:
        print(" "*(math.floor((int(linelen-wordcount))/2)-1), end='')
    else:
        print(" "*(math.floor((int(linelen-wordcount))/2)), end='')
    print("|")


    print("+--------------------------------+")

    for detail in listtoprint:
        wordcount = countword(detail)
        print("|", end='')
        print(" "*2, end='')
        print(detail, end='')
        usedspace = countword(detail)
        print(" "*(linelen-(wordcount + 4)), end='')
        print("|", end='')
        print("\n")

    print("+--------------------------------+")



def enterstddata():
    print("\n")

    print("To register a new student, enter the student's data as prompted.")
    name = input("Enter the student's name: ")
    rollno = int(input("Enter the roll number: "))
    classname = int(input("Enter the class: "))
    section = input("Enter the section: ")
    print("\n")
    print("Now, enter the marks of individual subjects as prompted.")
    try:
        markse = int(input("Marks in English: "))
        marksp = int(input("Marks in Physics: "))
        marksc = int(input("Marks in Chemistry: "))
        marksm = int(input("Marks in Maths: "))
        marksip = int(input("Marks in IP: "))
    except:
        print("Invalid value entered. Please enter an integer value from 0 to 100 only for marks in each subject.")
        return

    if classname > 12 or classname < 1:
        print("Class ", classname, " doesn't exist. Please try again with a valid class.")
        return
    

    studentseries = pd.Series([name, rollno, classname, section, markse, marksp, marksc, marksm, marksip],
                          index = ['Name', 'RollNo', 'Classname', 'Section', 'MarksinEnglish', 'MarksinPhysics', 'MarksinChemistry', 'MarksinMaths', 'MarksinIP'])


    with open("students.csv", "a") as file:
        for i, v in studentseries.items():
            entry = str(i) + ":" + str(v) + ","
            file.write(entry)
        file.write("\n")



def displayrecords():
    stddata = []
    j = 1
    with open('students.csv', 'r') as f:
        mycsv = csv.reader(f)
        for row in mycsv:
            i = 0
            print("\n")
            while i != 9:
                stddata.append(row[i])
                i+=1

            cleanprint(stddata, str("Student " + str(j) )) 
            j += 1 
            stddata = []



def searchstdbyrollno(rolltocheck):
    with open('students.csv', 'r') as f:
        mycsv = csv.reader(f)
        csvlist = list(mycsv)
        counter = 0
       
        flag = 0

        for row in csvlist:
            try:
                if str(row[1]) == rolltocheck:
                    flag = 1
                    break
                    #print(csvlist[counter])
                else:
                    counter+=1
            except:
                print("\n")
                print("Student not found")

        if flag == 1:
            return csvlist[counter]


def findtopperrollnum(classnum):
    classtocheck = 'Classname:' + str(classnum)
    counter = 0

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
        if classlist:
            for student in classlist:
                ineng = wordstoint(student[4])
                inphy = wordstoint(student[5])
                inchem = wordstoint(student[6])
                inmaths = wordstoint(student[7])
                inip = wordstoint(student[8])

                marks_of_all.append(int(ineng) + int(inphy) + int(inchem) + int(inmaths) + int(inip)) 

            max_marks, topper_index = findmaxandindex(marks_of_all)
            return (classlist[topper_index])[1]
        else:
            print("No student found in class.")
            return "None"



def displaytopper(classnum):
    classtocheck = 'Classname:' + str(classnum)
    counter = 0

    

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

        cleanprint(classlist[topper_index], "Topper's details")

        print("This student got", round((max_marks/500)*100, 2), "%")
        
        return topper_index



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
        avgeng = round(totale/(len(alleng)), 2)
        
        for marks in allphy:
            totalp+=int(marks)
        avgphy = round(totalp/(len(allphy)), 2)

        for marks in allchem:
            totalc+=int(marks)
        avgchem = round(totalc/(len(allchem)), 2)

        for marks in allmaths:
            totalm+=int(marks)
        avgmaths = round(totalm/(len(allmaths)), 2)

        for marks in allip:
            totali+=int(marks)
        avgip = round(totali/(len(allip)), 2)
        

        avgmarks = []

        avgmarks.append(f"Average in English: {avgeng}")
        avgmarks.append(f"Average in Physics: {avgphy}")
        avgmarks.append(f"Average in Chemistry: {avgchem}")
        avgmarks.append(f"Average in Maths: {avgmaths}")
        avgmarks.append(f"Average in IP: {avgip}")

        return avgmarks



def exportsummary():
    classnumlist = [11,12]     

    for classnum in classnumlist:
        rollnum = findtopperrollnum(int(classnum))
        cleanprint(searchstdbyrollno(rollnum), str("Topper in Class " + str(classnum)))
        print("\n")

    cleanprint(subavgmarks(), "Average Marks")


# print menu
print("Select an option:")
print("1. Enter new student data")
print("2. Display all records")
print("3. Search a student by roll number")
print("4. Display the topper of a given class")
print("5. Display subject-wise average marks of the whole school")
print("6. Export a summary of the records to a CSV file")


user_input = int(input("What do you want to do? Enter the number corresponding to the function you want to do: "))

if user_input == 1:
    enterstddata()
elif user_input == 2:
    displayrecords()
elif user_input == 3:
    print("\n")
    reqrollno = int(input("Which roll no.: "))
    rolltocheck = 'RollNo:' + str(reqrollno)
    cleanprint(searchstdbyrollno(rolltocheck), "Student details")
elif user_input == 4:
    classnum = int(input("From which class? : "))
    displaytopper(classnum)
    #print(wordstoint('MarksinEnglish:81'))
elif user_input == 5:
    cleanprint(subavgmarks(), "Average Marks")
elif user_input == 6:
    exportsummary()
else:
    print("This is not a valid option. Please enter a valid option.")
