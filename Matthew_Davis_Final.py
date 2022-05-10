import random
import re

#final exam
#Matthew Davis - 5/10/22

#QUESTION 1
print("Question 1\n")
lst=["z","m","n","a", "c", "i", "g", "x", "t"]

for i in range(0,len(lst)):
  for j in range (0,len(lst)):
    if lst[j]>lst[i]:
      temp=lst[i]
      lst[i]=lst[j]
      lst[j]=temp
print(lst)
print("\nQuestion 2\n")

#QUESTION 2
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

#QUESTION 4
class Clothing():
  def __init__(self,units,price):
    self.__description = description
    self.__units = str(units)
    self.__price = str(price)

def getDesc(self):
  return self.__description

def getUnits(self):
  return self.__units

def getPrice(self):
  return self.__price

def questSix():
  print("Part six: ")
  clothList = []
  temp = Clothing("Jacket", 40, 59.95)
  clothList.append(temp)
  temp = Clothing("Designer Jeans", 100, 24.95)
  clothList.append(temp)
  temp = Clothing("Shirt", 200, 24.95)
  clothList.append(temp)
  print(clothList)
  print("\n\n")

  outfile = open("clothing.txt", "w")
  for item in clothList:
    outfile.write(item.getDesc())
    outfile.write(" ")
    outfile.write(item.getUnits())
    outfile.write(" ")
    outfile.write(item.getPrice())
    outfile.write("\n")
  outfile.close()

#QUESTION 5
def bonus():
    string_test = "Hello my name is Rajesh, and my number is 123456789. My friend's name is Timmy, and his phone number is 987654321."
    
    names = re.findall("\ +[A-Z]+[a-z]+\,", string_test)
    numbers = re.findall("\s+[0-9]+\.", string_test)
    
    print(names)
    print(numbers)

# function to call in main
def question5a():
    # sets string and blank to modify with
    remove = '/*Jon is @developer & musician'
    modify = ""

    # for loop to remove symbols
    for ch in remove:
        if ch.isalpha() or ch.isspace():
            modify = modify + ch

    # prints string before and after modification
    print("String before modification: ", remove)
    print("String after modification: ", modify, "\n")

    # sets string and empty one to modify
    remove = 'Emma-is-a-data-scientist'
    modify = ""

    # for loop to remove symbols and replaced them with spaces
    for ch in remove:
        if ch == '-':
            modify = modify + ' '
        else:
            modify = modify + ch

    # prints string before and after modification
    print("String before modification: ", remove)
    print("String after modification: ", modify, "\n")
  
if __name__ == '__main__':
  print("\nQuestion 5\n")
  bonus()
  question5a()
  

#QUESTION 6
def computeFib(fibNum):
    #creating list to hold fib sequence
    fibSequence = []
    
    firstFib = 0
    secondFib = 1
    
    #Iterate from 0 to user input
    for temp in range(0, fibNum):
        #Append 1st and 2nd elements as 0 and 1 respectively
        if temp == 0:
            fibSequence.append(firstFib)
            continue
        if temp == 1:
            fibSequence.append(secondFib)
            continue
            
        #Append nextFib(sum of previous two numbers) and change firstFib
        #to secondFib and secondFib to nextFib
        nextFib = firstFib + secondFib
        firstFib = secondFib
        secondFib = nextFib
        fibSequence.append(nextFib)
    
    print("Fibonacci sequence for : ", fibSequence)
    print()
    
#Main function runs first method, second method with sample input, third method
#with provided list and fib sequence using user input
if __name__ == '__main__':
    print("\nQuestion 6\n")
    
    fibInput = int(input("Enter a number for fib sequence: "))
    computeFib(fibInput)
