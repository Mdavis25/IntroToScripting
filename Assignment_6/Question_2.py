# function to read file
def readFile(inFile):
    text = inFile.read()
    return text


# function to write to file
def writeFile(f1, f2, f3):
    # opens file to append
    inFile = open('final_file.txt', 'a')
    # reads and writes all passed strings into new file
    inFile.write(f1)
    inFile.write('\n')
    inFile.write(f2)
    inFile.write('\n')
    inFile.write(f3)
    # closes file
    inFile.close()


# function to call in main
def question2():
    # uses try block for exception
    try:
        # opens and reads each file
        f1 = open('f1.txt', 'r')
        f2 = open('f2.txt', 'r')
        f3 = open('f3.txt', 'r')
        write1 = readFile(f1)
        write2 = readFile(f2)
        write3 = readFile(f3)
        # closes files
        f1.close()
        f2.close()
        f3.close()
        # writes in new file
        writeFile(write1, write2, write3)
    # except error
    except FileNotFoundError:
        print("Error opening file")


# main
if __name__ == '__main__':
    question2()
