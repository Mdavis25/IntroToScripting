#gets pennies from user
pennies = input('How many pennies ')
#gets nickles from users
nickles = input('How many nickles ')
#gets dimes from user
dimes = input('How many dimes ')
#gets quarters from user
quarters = input('How many quarters ')
#gets value of nickles
nickles = int(nickles)*5
#gets values of dimes
dimes = int(dimes)*10
#gets values of quarters
quarters = int(quarters)*25
#gets total of change
total = int(pennies)+int(dimes)+int(quarters)+int(nickles)
#prints if you win
if int(total) == 100:
    print('Congratulations! You win!')
#prints if you lose
else:
    print('You lose.')