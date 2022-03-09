import re
import random


# student class
class Student:
    def __init__(self, fName, lName, eMail, cList):
        self.firstName = fName
        self.lastName = lName
        self.email = eMail
        self.allCourse = cList

    def __str__(self):
        return '{self.firstName} {self.lastName} {self.email} {self.allCourse}'.format(self=self)


# function to call in main
def question1():
    # opens file and reads it
    infile = open('students.txt', 'r')
    student = infile.read()
    # close file
    infile.close()

    # finds students first names
    stuFirstNames = re.findall('\n[A-Z]+[a-z]+\s', student)
    # for loop and regular expression to remove spaces and \n
    for num in range(0, len(stuFirstNames)):
        temp = stuFirstNames[num].rstrip()
        temp = temp.lstrip('\n')
        stuFirstNames[num] = temp

    # finds students last names
    stuLastNames = re.findall('\ +[A-Z]+[a-z]+\s', student)
    stuLastNames.pop(0)
    # uses for loop and regular express to find last name and set it to temp
    for num in range(0, len(stuLastNames)):
        temp = stuLastNames[num].rstrip()
        temp = temp.lstrip()
        stuLastNames[num] = temp

    # finds students emails
    Email = re.findall('[a-z]+@islander.tamucc.edu', student)

    # finds the course numbers and stores it in variable
    courseNum = re.findall('\d+,\d+,\d+,\d+,\d+,\d+\n', student)
    # appends stored variable
    courseNum.append(re.findall('\d+,\d+,\d+,\d+,\d+,\d+$', student)[0])

    # empty list to store
    listOne = []

    # for loop to extract student grades
    for numList in courseNum:
        tempList = [0, 0, 0, 0, 0, 0]
        temp = ""
        count = 0
        for ind in range(0, len(numList)):
            if not numList[ind].isdigit():
                tempList[count] = int(temp)
                count += 1
                temp = ""
            else:
                temp = temp + numList[ind]
                if ind == len(numList) - 1:
                    tempList[count] = int(temp)
        listOne.append(tempList)

    # empty list
    listOfStudents = []
    print("List of students gathered from original text file: ")
    # uses for loop to append students to the list
    for num in range(0, len(stuFirstNames)):
        tempStudent = Student(stuFirstNames[num], stuLastNames[num], Email[num], listOne[num])
        listOfStudents.append(tempStudent)
        print(listOfStudents[num])
    print("\n\n")

    # opens file
    outfile = open('students.txt', 'a')

    # names of students, last name will be blank
    tempFirst = "Child"
    tempLast = ""

    #
    print("Students being appended to file:")
    # for loop to write students on new file
    for i in range(0, 25):
        # write out to file
        outfile.write('\n')
        # last name will be student number
        tempLast = str(i)
        tempScores = [0, 0, 0, 0, 0, 0]
        # gives students random scores
        for n in range(0, 6):
            tempScores[i] = random.randint(0, 100)
        # writes students email
        tempEmail = tempFirst[0].lower() + str(tempLast) + "@islander.tamucc.edu"
        # creates student
        tempStudent = Student(tempFirst, tempLast, tempEmail, tempScores)
        # prints student
        print(tempStudent)
        # appends students to list
        listOfStudents.append(tempStudent)
        # writes students information to file
        outfile.write(tempFirst)
        outfile.write(" ")
        outfile.write(tempLast)
        outfile.write(" ")
        outfile.write(tempEmail)
        outfile.write(" ")
        for num in range(0, len(tempScores)):
            outfile.write(str(tempScores[num]))
            if num != len(tempScores) - 1:
                outfile.write(",")
    print("\n\n")
    # close file
    outfile.close()

    # sorts students in list
    listOfStudents.sort()
    print("Sorted list of students being added to final file:")
    for student in listOfStudents:
        print(student)

    # opens file to write
    stuSort = open('sorted_students.txt', 'w')
    # writes out student information into a new file
    for ind in range(0, len(listOfStudents)):
        stuSort.write(listOfStudents[ind].firstName)
        stuSort.write(" ")
        stuSort.write(listOfStudents[ind].lastName)
        stuSort.write(" ")
        stuSort.write(listOfStudents[ind].email)
        stuSort.write(" ")
        for num in range(0, len(listOfStudents[ind].allCourse)):
            stuSort.write(str(listOfStudents[ind].allCourse[num]))
            if num != len(listOfStudents[ind].allCourse) - 1:
                stuSort.write(",")
        if ind != len(listOfStudents) - 1:
            stuSort.write('\n')
    # closes file
    stuSort.close()


# main
if __name__ == '__main__':
    question1()
