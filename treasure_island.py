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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
choice1 = input('You\'ve come to a fork in the road. Where do you want to go? '
                'Type "left" or "right". ').lower()

if choice1 == "left":
    print("You hear the sounds of rushing water and raging winds. "
          "Eventually, moving along the path, you find yourself in front of a river. "
          "Would you like to: swim or wait")

    choice2 = input('Type "swim" or "wait". ').lower()
    if choice2 == "wait":
        print("The water eventually calms, and you cross safely. "
              "You wander down the path and find three colored doors in the middle of the forest. ")
        choice3 = input("Choose a door: "
                        "Red, Yellow, or Blue. ").lower()
        if choice3 == "red":
            print("You see a red room."
                  "The door closes behind you. You smell something like burnt trash and before you can exit\n"
                  "fire engulfs you from all sides.")
            print("Game Over.")
        elif choice3 == "blue":
            print("You see a blue room. "
                  "In the dark, you hear the growl of many unknown beasts. \n"
                  "Before you know it, dark shapes lunge from the dark and overwhelm you. \n"
                  "You have been eaten by beasts. \n"
                  "Game Over")
        elif choice3 == "yellow":
            print("You see a yellow room. \n"
                  "Bathed in gold ornaments and riches, and many fair maidens. \n"
                  "You have won the game! " "Congratulations!")


    elif choice2 == "swim":
        print("You try to swim, "
              "the current suddenly picks up and you muster all your energy to stay afloat. \n"
              "You are swept away by the water and drown. Game Over.")
        quit()
    else:
        print("Game Over.")


elif choice1 == "right":
    print("You walked off a cliff. "
          "Game Over.")

else:
    print("You can't go that way. Try Again.")
