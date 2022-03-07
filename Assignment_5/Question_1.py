def partOne():
    morseCode = {' ': ' ',
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

    userIn = input("Please enter a string to translate to morse code: ")

    translate = ""

    for ch in userIn:
        translate = translate + morseCode[ch.upper()]

    print("Morse code of ", userIn, " is ", translate)


if __name__ == '__main__':
    partOne()
