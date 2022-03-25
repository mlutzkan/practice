rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

user_choice = int(input("Type 0 for rock, 1 for paper or 2 for scissors. \n"))
computer_choice = random.randint(0,2)

if user_choice == 0:
  print("You chose ROCK")
  print(rock)
  if computer_choice == 1:
    print("Computer chose PAPER.")
    print(paper)
    print("YOU LOSE")
  elif computer_choice == 2:
    print("Computer chose SCISSORS.")
    print(scissors)
    print("YOU WIN!")
  else:
    print("So did the computer.")
    print("It's a tie.")

if user_choice == 1:
  print("You chose PAPER")
  print(paper)
  if computer_choice == 2:
    print("Computer chose SCISSORS.")
    print(scissors)
    print("YOU LOSE")
  elif computer_choice == 0:
    print("Computer chose ROCK.")
    print(rock)
    print("YOU WIN!")
  else:
    print("So did the computer.")
    print("It's a tie.")

if user_choice == 2:
  print("You chose SCISSORS.")
  print(scissors)
  if computer_choice == 0:
    print("Computer chose ROCK.")
    print(rock)
    print("YOU LOSE")
  elif computer_choice == 1:
    print("Computer chose PAPER.")
    print(paper)
    print("YOU WIN!")
  else:
    print("So did the computer.")
    print("It's a tie.")
    
