# imports random number
import random


# student class
class Student:
    def __init__(self, fName, lName, cList):
        # declares student variables
        self.firstName = fName
        self.lastName = lName
        self.courseList = cList

        self.percentage = self.calcPercentage()

    def __str__(self):
        return '{self.firstName} {self.lastName}\tPercentage: {self.percentage}'.format(self=self)

    # function to find Percent scores of students
    def calcPercentage(self):
        sum = 0
        for temp in self.courseList:
            sum += temp
        return sum / 600 * 100


# main
if __name__ == '__main__':
    # declaring list and variables
    stuList = []
    tempFirst = "Student"
    tempLast = ""

    # print
    print("Students Grade Percent: ")

    # finds students scores at random using loops
    for i in range(1, 26):
        tempLast = i
        tempScores = [0, 0, 0, 0, 0, 0]
        for j in range(0, 6):
            tempScores[j] = random.randint(0, 101)
        # appends them into a new list
        stuList.append(Student(tempFirst, tempLast, tempScores))
    # prints students grade from 1-25
    for temp in stuList:
        print(temp)
    print()

    # print
    print("Students Percent Grade Sorted: ")
    # creates a new list
    newList = []
    length = len(stuList)

    # while the length of the new list is not equal to the old list
    while len(newList) != length:
        smallestIndex = 0
        # sorts the list in order of percent
        for tempIndex in range(0, len(stuList)):
            if stuList[tempIndex].percentage < stuList[smallestIndex].percentage:
                smallestIndex = tempIndex
        tempVal = stuList.pop(smallestIndex)
        newList.append(tempVal)
    # prints students based on percent
    for temp in newList:
        print(temp)
    print()
    # print
    print("Course Averages: ")
    # new list for course averages
    courseAverages = [0, 0, 0, 0, 0, 0]
    # adds course averages in the list
    for temp in newList:
        for i in range(0, 6):
            courseAverages[i] += temp.courseList[i]
    # finds the averages by dividing
    for i in range(0, 6):
        courseAverages[i] = courseAverages[i] / 25
        print("Course ", i + 1, " Average: ", courseAverages[i])
