def getNumVows(someStr):
    count = 0

    for ch in someStr:
        if ch.upper() == 'A' or ch.upper() == 'E' or ch.upper() == 'I' or ch.upper() == 'O' or ch.upper() == 'U':
            count += 1

    return count


def getNumCons(someStr):
    count = 0

    for ch in someStr:
        if ch.isalpha() and ch.upper() != 'A' and ch.upper() != 'E' and ch.upper() != 'I' and ch.upper() != 'O' and ch.upper() != 'U':
            count += 1

    return count


def partTwo():
    userIn = input("Please enter a string to count vowels and consonants: ")
    print("Number of vowels in string: ", getNumVows(userIn))
    print("Number of consonants in string: ", getNumCons(userIn))


if __name__ == '__main__':
    partTwo()
