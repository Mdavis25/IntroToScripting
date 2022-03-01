# numList function
def numList():
    # creates empty list
    nList = []

    # for loop to enter numbers
    for num in range(0, 20):
        temp = int(input("Enter num to add to list: "))
        nList.append(temp)

    # prints list
    print(nList)
    # prints the smallest number in list
    print("Smallest number in the list: ", min(nList))
    # prints the largest number in list
    print("Largest number in the list: ", max(nList))
    # prints the sum of the list
    print("Total of numbers in the list: ", sum(nList))
    # prints the average of numbers in the list
    print("Average of numbers in the list: ", sum(nList) / len(nList))


# main to call function
if __name__ == '__main__':
    # function call
    numList()
