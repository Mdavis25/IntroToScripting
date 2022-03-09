import re
import random


class Student():
    def __init__(self, fName, lName, eMail, cList):
        self.firstName = fName
        self.lastName = lName
        self.email = eMail
        self.allCourse = cList

    def __str__(self):
        return '{self.firstName} {self.lastName} {self.email} {self.allCourse}'.format(self=self)


def question1():
    infile = open('students.txt', 'r')
    studentDetails = infile.read()
    infile.close()

    stuFnames = re.findall('\n[A-Z]+[a-z]+\s', studentDetails)
    for num in range(0, len(stuFnames)):
        temp = stuFnames[num].rstrip()
        temp = temp.lstrip('\n')
        stuFnames[num] = temp

    stuLnames = re.findall('\ +[A-Z]+[a-z]+\s', studentDetails)
    stuLnames.pop(0)
    for num in range(0, len(stuLnames)):
        temp = stuLnames[num].rstrip()
        temp = temp.lstrip()
        stuLnames[num] = temp

    stuEmails = re.findall('[a-z]+@islander.tamucc.edu', studentDetails)

    uneditedCourse = re.findall('\d+,\d+,\d+,\d+,\d+,\d+\n', studentDetails)
    uneditedCourse.append(re.findall('\d+,\d+,\d+,\d+,\d+,\d+$', studentDetails)[0])

    listOfLists = []

    for numList in uneditedCourse:
        tempList = [0, 0, 0, 0, 0, 0]
        temp = ""
        current = 0
        for ind in range(0, len(numList)):
            if not numList[ind].isdigit():
                tempList[current] = int(temp)
                current += 1
                temp = ""
            else:
                temp = temp + numList[ind]
                if ind == len(numList) - 1:
                    tempList[current] = int(temp)
        listOfLists.append(tempList)

    listOfStudents = []
    print("List of students gathered from original text file: ")
    for num in range(0, len(stuFnames)):
        tempStudent = Student(stuFnames[num], stuLnames[num], stuEmails[num], listOfLists[num])
        listOfStudents.append(tempStudent)
        print(listOfStudents[num])
    print("\n\n")

    outfile = open('students.txt', 'a')

    tempFirst = "Student"
    tempLast = ""

    print("Students being appended to file:")

    for i in range(0, 25):

        outfile.write('\n')

        tempLast = str(i)

        tempScores = [0, 0, 0, 0, 0, 0]
        for i in range(0, 6):
            tempScores[i] = random.randint(0, 100)

        tempEmail = tempFirst[0].lower() + str(tempLast) + "@islander.tamucc.edu"

        tempStudent = Student(tempFirst, tempLast, tempEmail, tempScores)
        print(tempStudent)
        listOfStudents.append(tempStudent)

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
    outfile.close()

    listOfStudents.sort(key=lambda x: x.firstName)
    print("Sorted list of students being added to final file:")
    for student in listOfStudents:
        print(student)

    sortout = open('sorted_students.txt', 'w')

    for ind in range(0, len(listOfStudents)):
        sortout.write(listOfStudents[ind].firstName)
        sortout.write(" ")
        sortout.write(listOfStudents[ind].lastName)
        sortout.write(" ")
        sortout.write(listOfStudents[ind].email)
        sortout.write(" ")
        for num in range(0, len(listOfStudents[ind].allCourse)):
            sortout.write(str(listOfStudents[ind].allCourse[num]))
            if num != len(listOfStudents[ind].allCourse) - 1:
                sortout.write(",")
        if ind != len(listOfStudents) - 1:
            sortout.write('\n')

    sortout.close()


if __name__ == '__main__':
    question1()
