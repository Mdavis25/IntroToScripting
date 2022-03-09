# function to call in main
def question3():
    # print
    print("Counting numbers of letters, digits, and symbols in P@#yn26at^&i5ve")

    # sets string and counters
    count = 'P@#yn26at^&i5ve'
    letterCount = 0
    digitCount = 0
    symbolCount = 0

    # for loop to count letters, digits and symbols
    for ch in count:
        # letters
        if ch.isalpha():
            letterCount += 1
        # numbers
        elif ch.isdigit():
            digitCount += 1
        # symbols
        else:
            symbolCount += 1

    # prints counts
    print("Number of letters: ", letterCount)
    print("Number of digits: ", digitCount)
    print("Number of symbols: ", symbolCount, "\n")

    # sets string and blank to modify with
    remove = '/*Jon is @developer & musician'
    modify = ""

    # for loop to remove symbols
    for ch in remove:
        if ch.isalpha() or ch.isspace():
            modify = modify + ch

    # prints string before and after modification
    print("String before modification: ", remove)
    print("String after modification: ", modify, "\n")

    # sets string and empty one to modify
    remove = 'Emma-is-a-data-scientist'
    modify = ""

    # for loop to remove symbols and replaced them with spaces
    for ch in remove:
        if ch == '-':
            modify = modify + ' '
        else:
            modify = modify + ch

    # prints string before and after modification
    print("String before modification: ", remove)
    print("String after modification: ", modify, "\n")

    # sets string and empty one to modify
    remove = 'Hello, have a good day'
    modify = ""

    # for loop to remove consonants from string
    for ch in remove:
        if ch.upper() == 'A' or ch.upper() == 'E' or ch.upper() == 'I' or ch.upper() == 'O' or ch.upper() == 'U' or ch.isspace():
            modify = modify + ch

    # prints string before and after modification
    print("String before modification: ", remove)
    print("String after modification: ", modify)


# main
if __name__ == '__main__':
    question3()
