def readFile(inFile):
    tempTxt = inFile.read()
    return tempTxt


def writeFile(one, two, three):
    inFile = open('final_file.txt', 'a')
    inFile.write(one)
    inFile.write('\n')
    inFile.write(two)
    inFile.write('\n')
    inFile.write(three)
    inFile.close()


def partTwo():
    try:
        inOne = open('f1.txt', 'r')
        inTwo = open('f2.txt', 'r')
        inThree = open('f3.txt', 'r')

        firstTxt = readFile(inOne)
        secondTxt = readFile(inTwo)
        thirdTxt = readFile(inThree)

        inOne.close()
        inTwo.close()
        inThree.close()

        writeFile(firstTxt, secondTxt, thirdTxt)
    except FileNotFoundError:
        print("Error opening file")


if __name__ == '__main__':
    partTwo()
