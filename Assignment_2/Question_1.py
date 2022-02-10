#First set of *, uses nested loop to print * followed by spaces using counter
for temp in range(1, 6):
    for temp2 in range(0,temp):
        print("*", end = " ")
    print()

#Second set of *, uses two nested loops to print spaces followed by * using a counter
for temp in range(1, 6):
    for temp2 in range(0, 5 - temp):
        print(end = "  ")
    for temp3 in range(0, temp):
        print("*", end = " ")
    print()
