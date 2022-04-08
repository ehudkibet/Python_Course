from random import randint
t=["Paper","Rock","Scissors"]
computer=t[randint(0,2)]
player = False

while player ==False:
    player=input("Rock, Papers or Scissors? ").capitalize()
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose", computer , "covers", player)
        elif computer == "Scissors":
            print("You win", player,"smashes" , computer)
    elif player == "Paper":
        if computer == "Rock":
            print("You win", player , "covers", computer)
        elif computer == "Scissors":
            print("You lose", computer,"cuts" , player)
    elif player == "Scissors":
        if computer == "Paper":
            print("You win", player , "cuts", computer)
        elif computer == "Rock":
            print("You lose", computer,"smashes" , player)
    else:
        print("That's not a valid play. Check the spelling!")
