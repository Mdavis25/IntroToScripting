import random


class Student:
    def __init__(self, fName, lName, cList):
        self.firstName = fName
        self.lastName = lName
        self.courseList = cList

        self.percentage = self.calcPercentage()

    def __str__(self):
        return '{self.firstName} {self.lastName}\tPercentage: {self.percentage}'.format(self=self)

    def calcPercentage(self):
        sum = 0
        for temp in self.courseList:
            sum += temp
        return sum / 600 * 100


if __name__ == '__main__':
    stuList = []
    tempFirst = "Student"
    tempLast = ""

    print("Students Grade Percent: ")

    for i in range(1, 26):
        tempLast = i
        tempScores = [0, 0, 0, 0, 0, 0]
        for i in range(0, 6):
            tempScores[i] = random.randint(0, 100)
        stuList.append(Student(tempFirst, tempLast, tempScores))

    for temp in stuList:
        print(temp)
    print()

    print("Students Percent Grade Sorted: ")

    newList = []
    length = len(stuList)

    while len(newList) != length:
        smallestIndex = 0
        for tempIndex in range(0, len(stuList)):
            if stuList[tempIndex].percentage < stuList[smallestIndex].percentage:
                smallestIndex = tempIndex
        tempVal = stuList.pop(smallestIndex)
        newList.append(tempVal)

    for temp in newList:
        print(temp)
    print()

    print("Course Averages: ")

    courseAverages = [0, 0, 0, 0, 0, 0]

    for temp in newList:
        for i in range(0, 6):
            courseAverages[i] += temp.courseList[i]

    for i in range(0, 6):
        courseAverages[i] = courseAverages[i] / 25
        print("Course ", i + 1, " Average: ", courseAverages[i])
