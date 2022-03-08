def partFive():
    mainStr = "this is the string for the class"

    copyOne = ""
    copyTwo = ""
    copyThree = ""
    copyFour = ""

    beforeNum = 0

    for num in range(0, len(mainStr)):

        if num == 0:
            copyOne = copyOne + mainStr[num].upper()

        elif mainStr[beforeNum] == ' ':
            copyOne = copyOne + mainStr[num].upper()

        else:
            copyOne = copyOne + mainStr[num]

        beforeNum = num

    print(copyOne)

    for ch in copyOne:

        if ch != ' ':
            copyTwo = copyTwo + ch

    print(copyTwo)

    for ch in copyOne:

        if ch == 's':
            copyThree = copyThree + '$'

        else:
            copyThree = copyThree + ch

    print(copyThree)

    beforeNum = 0

    for num in range(0, len(mainStr)):

        if num == 0:
            copyFour = copyFour + mainStr[num].upper()

        elif mainStr[beforeNum] == ' ' and mainStr[num] == 's' or mainStr[num] == 'c':
            copyFour = copyFour + mainStr[num].upper()

        else:
            copyFour = copyFour + mainStr[num]

        beforeNum = num

    # print the new string
    print(copyFour)


if __name__ == '__main__':
    partFive()
