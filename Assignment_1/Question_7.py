#user enters weight
weight = input('Enter your weight ')
#user enters height
height = input('Enter your height ')
#finds bmi
bmi = int(weight)*703/int(height)**2
#finds if user is underweight, overweight or optimal
if bmi < 18.5:
    print('Underweight')
if bmi >= 18.5 <= 25:
    print('Optimal')
if bmi > 25:
    print('Overweight')