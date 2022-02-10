#setting lists to be sorted
List = [20, 68, 41, 88, 16, 40, 65, 97, 85]
newList = []

#sets length equal to the number of items in List
length = len(List)

#while the length of newList is not equal to the length, this loop will run
while len(newList) != length:
    #setting a zero to check the first spot in the list
    smallestIndex = 0
    #loop to go through list
    for tempIndex in range(0, len(List)):
        #if the second number is smaller then the first, it makes the first second number the smallest
        if (List[smallestIndex] > List[tempIndex]):
            smallestIndex = tempIndex
    #removes smallest number from the old list
    tempVal = List.pop(smallestIndex)
    #adds smallest number to the new list
    newList.append(tempVal);

#prints old and new lists
print("Old list: ", List)
print("Sorted list: ", newList);