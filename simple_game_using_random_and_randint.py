from random import randint

t = ["Rock", "Paper", "Scissors"] # create 3 options

computer = t[randint(0,2)] # assign random play for computer
player = False
while player == False:

    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose...", computer, "covers", player)
        else:
            print("You win...", player, "cracks", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win...", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "cracks", player)
        else:
            print("You win...", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

    player = False
    computer = t[randint(0,2)]from random import randint

t = ["Rock", "Paper", "Scissors"] # create 3 options

computer = t[randint(0,2)] # assign random play for computer
player = False
while player == False:

    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose...", computer, "covers", player)
        else:
            print("You win...", player, "cracks", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win...", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "cracks", player)
        else:
            print("You win...", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

    player = False
    computer = t[randint(0,2)]from random import randint

t = ["Rock", "Paper", "Scissors"] # create 3 options

computer = t[randint(0,2)] # assign random play for computer
player = False
while player == False:

    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose...", computer, "covers", player)
        else:
            print("You win...", player, "cracks", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win...", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "cracks", player)
        else:
            print("You win...", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

    player = False
    computer = t[randint(0,2)]