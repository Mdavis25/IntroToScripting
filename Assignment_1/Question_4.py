#user enters age
age = input('Enter your age ')
#if user enters less than 1, says infant
if int(age) <= 1:
    print('Infant')
# if user enters less than 13, says child
if int(age) > 1 < 13:
     print('Child')
# if user enters more 13 and less than 20, says teenager
if int(age) >= 13 < 20:
    print('Teenager')
# if user enters more than 20, says adult
if int(age) > 20:
    print('Adult')