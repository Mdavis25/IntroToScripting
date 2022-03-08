import math


def partFour():
    badInput = True
    while badInput:
        numOfIns = input("Enter a number greater than 10: ")
        if not numOfIns.isdigit() or int(numOfIns) <= 10:
            print("Invalid input, try again")
        else:
            badInput = False

    listOfIns = []

    for num in range(0, int(numOfIns)):

        badInput = True

        while badInput:
            temp = input("Enter a number between 0-100: ")
            if not temp.isdigit() or int(temp) < 0 or int(temp) > 100:
                print("Invalid input, try again")
            else:
                badInput = False

        listOfIns.append(int(temp))

    print("List of integers: ", listOfIns)

    avg = sum(listOfIns) / len(listOfIns)
    print("Average of list: ", avg)

    sortedList = listOfIns.copy()
    sortedList.sort()

    if len(sortedList) % 2 == 0:
        firstMiddle = (len(sortedList) + 1) / 2
        secondMiddle = (len(sortedList) + 1) / 2 + 1
        median = (sortedList[firstMiddle] + sortedList[secondMiddle]) / 2

    else:
        middle = int((len(sortedList) + 1) / 2 - 1)
        median = sortedList[middle]

    print("Median of list: ", median)

    stdDev = 0

    for num in listOfIns:
        stdDev += (num - avg) ** 2

    stdDev /= len(listOfIns) - 1

    stdDev = math.sqrt(stdDev)

    print("Standard deviation of list: ", stdDev)

    divList = []
    try:

        for num in range(0, len(listOfIns) - 1):
            temp = listOfIns[num] / listOfIns[num + 1]
            divList.append(temp)
    except:

        print("An exception has occurred creating the division list")

    print("Division list: ", divList)


if __name__ == '__main__':
    partFour()
