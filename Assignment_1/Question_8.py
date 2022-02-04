#variables
shares = 2000
stock = 40
commission = 0.03
sold = 42.75
#finding and printing amounts
print('Joe paid', shares*stock, 'for the stock')
print('Joe paid the broker', shares*stock*commission, 'for the stock')
print('Joe sold the stock for', shares*sold)
print('Joe paid the broker', sold*shares*commission, 'for selling the stock')
print('Joe made', shares*stock+(shares*stock*commission)-shares*sold+(sold*shares*commission))
#if statement to find if there was profit
if shares*stock+(shares*stock*commission)-shares*sold+(sold*shares*commission) > 0:
    print('Joe made a profit')
else:
    print('Joe lost money')