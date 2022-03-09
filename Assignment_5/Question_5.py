# function to call in main
def question5():
    # main string
    mainStr = "this is the string for the class"

    stringOne = ""
    stringTwo = ""
    stringThree = ""
    stringFour = ""

    count = 0

    # uses a for loop to go through string
    for num in range(0, len(mainStr)):
        # changes the first letter to a capital
        if num == 0:
            stringOne = stringOne + mainStr[num].upper()
        # changes the first letter of each word after the space to a capital
        elif mainStr[count] == ' ':
            stringOne = stringOne + mainStr[num].upper()
        # copies the rest of the sentence
        else:
            stringOne = stringOne + mainStr[num]
        count = num
    # prints new string
    print(stringOne)

    # for loop to remove spaces in sentence
    for ch in stringOne:
        if ch != ' ':
            stringTwo = stringTwo + ch
    # prints new string
    print(stringTwo)

    # for loop to change all the s in string to $
    for ch in stringOne:
        if ch == 's':
            stringThree = stringThree + '$'
        else:
            stringThree = stringThree + ch
    # prints new string
    print(stringThree)
    count = 0

    # for loop to change some letters into uppercase
    for num in range(0, len(mainStr)):
        # changes the first letter to uppercase
        if num == 0:
            stringFour = stringFour + mainStr[num].upper()
        # changes the S and C to uppercase
        elif mainStr[count] == ' ' and mainStr[num] == 's' or mainStr[num] == 'c':
            stringFour = stringFour + mainStr[num].upper()
        # copies the rest of the string
        else:
            stringFour = stringFour + mainStr[num]
        count = num
    # prints the string
    print(stringFour)


# main
if __name__ == '__main__':
    question5()
