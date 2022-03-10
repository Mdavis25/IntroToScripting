import random

""""
Answers for true or false
"""
# Question 1: True
# Question 2: True
# Question 3: False
# Question 4: False
# Question 5: False
# Question 6: True
# Question 7: True
# Question 8: True
# Question 9: False
# Question 10: False

"""
Answers for one or two statement
"""

# Question 1: Repetition structures are loops which can be used to run the same code multiple times. Decision
# structures are excecuted once based on a condition.

# Question 2: A class creates an object and holds variables associated with them. An instance of a class is a
# specific object and variables within the code.

# Question 3: A recursion function calls itself within itself

# Question 4: Open the file, Read the file, Close the file

# Question 5: When a new class is made from a parent class and uses its properties. The subclass inherits everything
# from its super class.


"""
Coding challenges
"""
# Question 1:
print("Even")
for temp in range(1, 51):
    if temp % 2 == 0:
        print(temp)
print("\nOdd")
for temp in range(1, 51):
    if temp % 2 != 0:
        print(temp)

# Question 2:
numList = []
for num in range(0, 20):
    temp = random.randint(0, 100)
    numList.append(temp)
print("List: ", numList)
numList.sort()
print("Sorted List: ", numList)
numList.sort(reverse=True)
print("Reverse Sorted List: ", numList)

# Question 3:
stuDict = {"Matt": [60, 75, 98, 54, 100, 94],
           "Kody": [100, 97, 80, 79, 83, 88],
           "Tristan": [68, 39, 56, 92, 86, 10]}

# Question 4:
TypeA = 20
TypeB = 15
TypeC = 10
total = 0


def question4():
    sold = int(input("How many Type A seats were sold? "))
    tickTotal = (TypeA * sold)
    sold = int(input("How many Type B seats were sold? "))
    tickTotal = (TypeB * sold) + tickTotal
    sold = int(input("How many Type C seats were sold? "))
    tickTotal = (TypeC * sold) + tickTotal
    print(tickTotal)


# Question 5:
def findSecondLargest(numberList):
    largest = 0
    secondLargest = 0

    for n in range(1, len(numberList)):
        if numberList[n] > numberList[largest]:
            secondLargest = largest
            largest = n
        elif numberList[secondLargest] < numberList[n] < numberList[largest]:
            secondLargest = n

    return numberList[secondLargest]


def removeDuplicates(numberList):
    woDuplicates = []

    for n in numberList:
        if num not in woDuplicates:
            woDuplicates.append(n)
    return


def question5():
    print("Second largest number: ", findSecondLargest(numList))


# Question 6:
class Brand:
    def __init__(self, desc, units, price, idNum):
        self.clothing = desc
        self.units = units
        self.price = price
        self.idNumber = idNum

    def __str__(self):
        return 'Clothing: {self.clothing} \nunits: {self.units}\nprice: {self.price}\nIdNumber: {self.idNumber}\n'.format(self=self)


brandDict = {}
tempClothing = "Jacket"
tempUnit = 40
tempPrice = 59.95
tempid = 1
tempBrand = Brand(tempClothing, tempUnit, tempPrice, tempid)
brandDict[tempid] = tempBrand

print(brandDict[tempid])

tempClothing = "Designer Jeans"
tempUnit = 100
tempPrice = 34.95
tempid = 2
tempBrand = Brand(tempClothing, tempUnit, tempPrice, tempid)
brandDict[tempid] = tempBrand

print(brandDict[tempid])

tempClothing = "Shirt"
tempUnit = 200
tempPrice = 24.95
tempid = 3
tempBrand = Brand(tempClothing, tempUnit, tempPrice, tempid)
brandDict[tempid] = tempBrand

print(brandDict[tempid])

# Question 7:
count = 0
uin = input("Provide an input: ")
if uin.isdigit():
    print(uin)
elif uin.isalpha():
    for ch in uin:
        if ch != ' ':
            uin = uin + ch
    print(uin)
    if uin.upper() == 'T':
        count = count + 1


    # Question 8:


# Bonus question:


if __name__ == '__main__':
    question4()
    question5()
