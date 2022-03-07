def partThree():
    print("Counting numbers of letters, digits, and symbols in P@#yn26at^&i5ve")

    strOne = 'P@#yn26at^&i5ve'
    letterCount = 0
    digitCount = 0
    symbolCount = 0

    for ch in strOne:
        if ch.isalpha():
            letterCount += 1
        elif ch.isdigit():
            digitCount += 1
        else:
            symbolCount += 1

    print("Number of letters: ", letterCount)
    print("Number of digits: ", digitCount)
    print("Number of symbols: ", symbolCount, "\n")

    strTwo = '/*Jon is @developer & musician'
    modTwo = ""

    for ch in strTwo:
        if ch.isalpha() or ch.isdigit() or ch.isspace():
            modTwo = modTwo + ch

    print("String before modification: ", strTwo)
    print("String after modification: ", modTwo, "\n")

    strThree = 'Emma-is-a-data-scientist'
    modThree = ""

    for ch in strThree:
        if ch == '-':
            modThree = modThree + ' '
        else:
            modThree = modThree + ch

    print("String before modification: ", strThree)
    print("String after modification: ", modThree, "\n")

    strFour = 'Hello, have a good day'
    modFour = ""

    for ch in strFour:
        if ch.upper() == 'A' or ch.upper() == 'E' or ch.upper() == 'I' or ch.upper() == 'O' or ch.upper() == 'U' or ch.isspace():
            modFour = modFour + ch

    print("String before modification: ", strFour)
    print("String after modification: ", modFour)


if __name__ == '__main__':
    partThree()
