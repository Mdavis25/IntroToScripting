#setting new list
newList = [16, 20, 40, 41, 65, 68, 85, 88, 97]

#initailizes the sum
sum = 0

#uses for loop to add all the numbers in the list
for temp in newList:
    sum += temp

#prints the sum
print("Sum of List: ", sum)

#makes a new list for even numbers
evenList = []

#uses for loop and if statement to find the even numbers in the list, appends them to a new list
for temp in newList:
    if temp % 2 == 0:
        evenList.append(temp)

#prints even list
print("Even List: ", evenList)

#finds the sum of the even numbers
sum = 0
for temp in evenList:
    sum += temp

#prints even numbers
print("Sum of even list: ", sum)

#makes new list for odd numbers
oddList = []

#uses for loop and if statement to find the odd numbers in the list, appends them to a new list
for temp in newList:
    if temp % 2 == 1:
        oddList.append(temp)

#prints odd numbers
print("Odd list: ", oddList)

#finds the sum of all the odd numbers
sum = 0
for temp in oddList:
    sum += temp

#prints the odd numbers
print("Sum of odd list: ", sum)
