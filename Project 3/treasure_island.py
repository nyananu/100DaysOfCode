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

# Print welcome message
print("Welcome to Treasure Island. Your mission is to find the treasure. \n")

# Prompt messages and program

path = (input("You are at a crossroad. Which path will you choose? Right or Left? \n")).lower()

if (path == "right"):
  print("You fell into a hole. Game Over.")

elif (path == "left"):
  action = (input("You reach a river. You might have to wait for a boat. What will you do? Wait or Swim\n")).lower()

  if (action == "swim"):
    print("You were attacked by a croc. Game Over.")

  elif (action == "wait"):
    door = (input("You were boated to safety and now face 3 doors, which one will you open? Red, Blue or Yellow? \n")).lower()

    if (door == "red"):
      print("You were burned by fire. Game Over.")

    elif (door == "blue"):
      print("You were eaten by beasts. Game Over.")

    elif (door == "yellow"):
      print("You Win!")
      
    else:
      print("You did not make a valid choice. Game Over.")




