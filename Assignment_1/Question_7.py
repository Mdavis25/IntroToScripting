weight = input('Enter your weight ')
height = input('Enter your height ')
bmi = int(weight)*703/int(height)**2
if bmi < 18.5:
    print('Underweight')
if bmi >= 18.5 <= 25:
    print('Optimal')
if bmi > 25:
    print('Overweight')