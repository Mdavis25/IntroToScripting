#User enters numbers to factorial, finds the difference
numN = int(input("Enter First Number: "))
numR = int(input("Enter Second Number: "))
diff = numN - numR

#sets factorial for loop counters
factN = 1
factR = 1
factDiff = 1

#finds factorial of N
for temp in range(1, numN+1):
    factN = factN * temp

#finds factorial of R
for temp in range(1, numR+1):
    factR = factR * temp

#Calculates the difference of N and R then factorials it
for temp in range(1, diff+1):
    factDiff = factDiff * temp

#finds total of (n-r)!
total = factR*factDiff

#prints total
print("n!/(r!(n-r)!) is equal to: ", factN/(factR*total))
print("n!/(n-r)! is equal to: ", factN/factDiff)
