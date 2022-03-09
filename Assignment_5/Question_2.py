# function to find Vowels
def VowelCounter(uInput):
    count = 0
    # for loop to count vowels in the string
    for ch in uInput:
        if ch.upper() == 'A' or ch.upper() == 'E' or ch.upper() == 'I' or ch.upper() == 'O' or ch.upper() == 'U':
            count += 1
    # returns count
    return count


# function to find consonants
def ConCounter(uInput):
    count = 0
    # for loop to count consonants in the string
    for ch in uInput:
        if ch.isalpha() and ch.upper() != 'A' and ch.upper() != 'E' and ch.upper() != 'I' and ch.upper() != 'O' and ch.upper() != 'U':
            count += 1
    # returns count
    return count


# function to call in main that will call other functions
def Counter():
    uInput = input("Enter a string to count consonants and vowels: ")
    print("Number of vowels in the string: ", VowelCounter(uInput))
    print("Number of consonants in the string: ", ConCounter(uInput))


# main
if __name__ == '__main__':
    Counter()
