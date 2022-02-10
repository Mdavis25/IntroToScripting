#prints "All prime numbers between 2 and 50:"
print("All prime numbers between 2 and 50:")

#For loop for numbers 2-50
for temp in range(2, 51):
    #Sets number as Prime
    isPrime = True
    #For loop for numbers 2-50
    for n in range(2, temp):
        #Sets number as not Prime if number is divisable by another number between 2-50
        if temp % n == 0:
            isPrime = False
    #Prints the number if it is prime
    if isPrime == True:
        print(temp)
