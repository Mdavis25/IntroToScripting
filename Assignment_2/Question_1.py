#
for temp in range(1, 6):
    for temp2 in range(0,temp):
        print("*", end = " ")
    print()

#
for temp in range(1, 6):
    for temp2 in range(0, 5 - temp):
        print(end = "  ")
    for temp3 in range(0, temp):
        print("*", end = " ")
    print()
