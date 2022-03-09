# morse code class to call in main
def MorseCode():
    # morse code dictionary
    charDict = {' ': ' ',
                ',': '--..--',
                '.': '.-.-.-',
                '?': '..--..',
                '0': '-----',
                '1': '.----',
                '2': '..---',
                '3': '...--',
                '4': '....-',
                '5': '.....',
                '6': '-....',
                '7': '--...',
                '8': '---..',
                '9': '----.',
                'A': '.-',
                'B': '-...',
                'C': '-.-.',
                'D': '-..',
                'E': '.',
                'F': '..-.',
                'G': '--.',
                'H': '....',
                'I': '..',
                'J': '.---',
                'K': '-.-',
                'L': '.-..',
                'M': '--',
                'N': '-.',
                'O': '---',
                'P': '.--.',
                'Q': '--.-',
                'R': '.-.',
                'S': '...',
                'T': '-',
                'U': '..-',
                'V': '...-',
                'W': '.--',
                'X': '-..-',
                'Y': '-.--',
                'Z': '--..'}

    # User inputs string to be translated
    uInput = input("Please enter a string to translate to morse code: ")

    # holds the morse code while each letter is translated
    translate = ""

    # for loop to translate from dictionary
    for ch in uInput:
        translate = translate + charDict[ch.upper()]

    # prints translated string
    print("Morse code of ", uInput, " is ", translate)


# main to call morse code function
if __name__ == '__main__':
    MorseCode()
