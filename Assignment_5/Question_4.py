import math


# function to call in main
def question4():
    # flag for input validation
    badInput = True
    # validation check
    while badInput:
        # user input
        numOfIns = input("Enter a number greater than 10: ")
        # if the user input is not a number or greater than or equal to 10
        if not numOfIns.isdigit() or int(numOfIns) <= 10:
            print("Invalid input, try again")
        else:
            badInput = False

    # list for numbers for user to input
    inputList = []

    # for loop that loops as long as user entered
    for num in range(0, int(inputList)):

        badInput = True

        # validation check
        while badInput:
            # user enters numbers between 0-100
            temp = input("Enter a number between 0-100: ")
            # if the input isn't a number or is less than 0 or greater than 100
            if not temp.isdigit() or int(temp) < 0 or int(temp) > 100:
                print("Invalid input, try again")
            else:
                badInput = False

        # numbers are appended into the list
        inputList.append(int(temp))

    # prints list
    print("List of integers: ", inputList)

    # finds and prints average
    avg = sum(inputList) / len(inputList)
    print("Average of list: ", avg)

    # makes a copy of the list to sort and alter
    sortedList = inputList.copy()
    # sorts list
    sortedList.sort()

    # finds median
    if len(sortedList) % 2 == 0:
        firstMiddle = (len(sortedList) + 1) / 2
        secondMiddle = (len(sortedList) + 1) / 2 + 1
        median = (sortedList[firstMiddle] + sortedList[secondMiddle]) / 2
    else:
        middle = int((len(sortedList) + 1) / 2 - 1)
        median = sortedList[middle]

    # prints median
    print("Median of list: ", median)

    # sets standard deviation = 0
    sDeviation = 0

    # math to find standard deviation
    for num in inputList:
        sDeviation += (num - avg) ** 2
    sDeviation /= len(inputList) - 1
    sDeviation = math.sqrt(sDeviation)

    # prints standard deviation
    print("Standard deviation of list: ", sDeviation)

    # creates empty list
    divList = []
    # try block for any type of exception
    try:
        for num in range(0, len(inputList) - 1):
            temp = inputList[num] / inputList[num + 1]
            divList.append(temp)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("That value was invalid.")

    # prints list
    print("Division list: ", divList)


# main
if __name__ == '__main__':
    question4()
