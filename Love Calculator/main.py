import time

print('Hi, welcome to Love Calculator!\nPlease note that this app is made for recreational purposes only and should not be relied upon for crucial decisions. \n \nGood luck!\n\n\n')

name1 = input('What is your name? \n')

name2 = input(f'\nHi {name1}, what is your crush\'s name? \n')



print(f'\nCalculating the love score for {name1} and {name2}, please wait...\n\n')
time.sleep(3)
print(f'\nCalculating the love score for {name1} and {name2}, please wait...\n\n')
time.sleep(3)
print(f'\nCalculating the love score for {name1} and {name2}, please wait...\n\n')
time.sleep(3)

name1_lower = name1.lower()
name2_lower = name2.lower()

combined_name = name1_lower + name2_lower

t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')

true = t + r + u + e

l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')

love = l + o + v + e

true_love = str(true) + str(love)
result = int(true_love)

if result < 10 or result > 90:
  print(f"Your love score is {result}. You go together like coke and menthos.")
elif result >= 40 and result <= 50:
  print (f"Your love score is {result}. You are alright together.")
else:
  print(f"Your love score is {result}.")



