# random number generator
import random


# find Second-Largest function
def findSecondLargest(numberList):
    # set largest equal to 0
    largest = 0
    # set second-largest equal to 0
    secondLargest = 0

    # for loop to go through list
    for num in range(1, len(numberList)):
        # set largest to larger number and second largest to largest
        if numberList[num] > numberList[largest]:
            secondLargest = largest
            largest = num
        elif numberList[secondLargest] < numberList[num] < numberList[largest]:
            secondLargest = num

    # returns the second-largest number
    return numberList[secondLargest]


def removeDuplicates(numberList):
    # list to remove dupes
    woDuplicates = []

    #
    for num in numberList:
        #
        if num not in woDuplicates:
            woDuplicates.append(num)

    #
    return woDuplicates


# random function
def Random():
    # new list
    numListTwo = []

    # finds 100 random numbers between 1-20 and adds to list
    for num in range(0, 100):
        temp = random.randint(0, 20)
        numListTwo.append(temp)

    # prints list of random numbers
    print("100 random numbers with range 0-20:")
    print(numListTwo)

    # prints second-largest number
    print("Second largest number: ", findSecondLargest(numListTwo))
    # prints list with duplicates removed
    print("List without duplicate elements: ", removeDuplicates(numListTwo))


# main to call function
if __name__ == '__main__':
    # function call
    Random()
