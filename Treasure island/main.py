print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print('''
  It is a bright, sunny day. You wake up on a deserted island and try to remember how you got there, but it is all a blur. The remains of a wrecked boat near the shore start to dig out some memories. That's right! The treasure! You went with a small group of adventurers to see if the legends were true. But it seems you are the only one left after the horrible storm. Now, will you perish on this creepy island, or will you find a way to get back home, richer than you could have ever imagined, is up to you.
      Let's find out!   



You follow a narrow path that comes to a crossroad. Everything else is filled with high and dense plants that you do not recognize. It seems that you only have two options - left or right.
''')

question1 = input("Which path would you take? Left or right? ").lower()

if question1 == "left":
  print ("You choose to go left. You walk until you reach a big river and there is nowhere else to go, but across. You see a small boat in the distance, but there is no way to tell if whoever is in it is friendly. You could wait and find out or swim across the river. Time to make another choice!")
  question2 = input("Swim or wait? ").lower()
  if question2 == "wait":
    print('''You wait as the boat gets closer.
  -Hey, you need a ride across? - says the stranger.
You agree and thank him.
-You're not from around here, are you?
-Not really - you say. - Actually, my boat just crashed here and I'm not even sure where I am.
-Welcome to the Island of the Dead. Many people come here to search for the treasure. I don't know if it exists, but I know that no one has lived to find out. Anyway, here we are. I'm going back to my hut down the river. You seem like a nice fella, I hope you don't die too soon. Good luck!
You get out of the boat and thank him again. "Oh, and choose wisely!", the stranger says as he start rowing away.
You keep going further into the island until you see three towers made of pure gold. Surely, the treasure must be in one of them! They are all identical, except for the different colours of their doors - blue, green and red.''')
    question3 = input("Which door do you choose - blue, green or red? ").lower()
    if question3 == "red":
      print("You open the red door. As soon as you do, a burst of flames consumes you, turning yor body into a pile of ash.")
      print("GAME OVER.")
    elif question3 == "blue":
      print("As soon as you open the door, you hear a mesmerizing roar. A huge beasts jumps towards you and tears away the flesh from your neck in a matter of seconds.")
      print("GAME OVER.")
    else:
      print('''You close your eyes and hold your breath as you open the door."Choose wisely!", the stranger's words ring in your head. For a second, you are certain that this is the end of your journey. And your life, for that matter. You open your eyes and take some time to decide if they are lying to you... No, your eyes are fine, it is true! Gold, jewels and gems - more than you could have ever imagined! Time to find the stranger - no doubt, he would gladly lend you his boat or join you on your way back home as the richest man in the world.''' )
      print("YOU WIN!")
  else:
    print("You get in the water and start swimming. You are nearly halfway there, when you see something stirring the water nearby. It quickly gets closer. You realize what it is, but it is too late. The piranhas are already having a feast...")
    print("Game over!")
else: 
  print("You make a few steps, when you suddenly the ground beneath the thick layer of leaves collapses. You fall into a deep hole and break your leg. You will either die here or wait for whoever set this trap to find you. It's hard to tell which one would be better.")
  print("            GAME OVER.")
