# numDictFunction function
def numDictFunction():
    # creates dictionary
    numDict = {}
    # user enters number
    n = int(input("Enter a number n: "))

    # creates dictionary from 1-n
    for num in range(1, n):
        numDict[num] = num * num

    # prints dictionary
    print(numDict)


# main to call function
if __name__ == '__main__':
    # function call
    numDictFunction()
