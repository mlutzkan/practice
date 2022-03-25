pizza_size = input('Please choose the size of your pizza (S for small, M for medium or L for large:\n') 
bill = 0
pepperoni = 0
extra_cheese = 1

if pizza_size == 'S' or pizza_size == 's':
  bill = 12
  pepperoni = 2
elif pizza_size == 'M' or pizza_size == 'm':
  bill = 20
  pepperoni = 3
else:
  bill = 25
  pepperoni = 3

wants_pepperoni = input('Would you like pepperoni on your pizza? Y or N:\n')

if wants_pepperoni == 'Y' or wants_pepperoni == 'y':
  bill = bill + pepperoni

wants_cheese = input ('Would you like extra cheese? Y or N:\n')

if wants_cheese == 'Y' or wants_cheese == 'y':
  bill = bill + extra_cheese


print(f'Your total bill is: ${bill}')








