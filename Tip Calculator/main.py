#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("How much is the bill? "))
number_of_people = int(input("How many people are splitting the bill? "))
tip_percentage = int(input("What tip would you like to leave - 10, 12 or 15 percent? ")) / 100
tip = bill * tip_percentage
result = (bill + tip) / number_of_people
result_rounded = round(result, 2)
print(f'You should each leave ${result_rounded}')

