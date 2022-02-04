#user inputs year
year = input('Enter a year ')
#finds if year is leap year or not
if int(year) % 100 == 0:
    if int(year) % 400 == 0:
        print(year, 'is a leap year')
if int(year) % 4 == 0:
    if int(year) % 100 != 0:
        print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')
