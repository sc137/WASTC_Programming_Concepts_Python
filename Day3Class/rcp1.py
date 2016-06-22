import random
play = "y"
cScore = 0
uScore = 0
while play == "y":
    computer = random.randint(0,2)

    userChoice = "spock"
    computerChoice = "spock2"
    print("Choose [R]ock, [P]aper, or [S]cissors: ", end="")
    user = "t"
    while user.lower() == "t":
            user = input()
            user = user.lower()
            if user == "r":
                userChoice = "Rock"
            elif user == "p":
                userChoice = "Paper"
            elif user == "s":
                userChoice = "Scissors"
            elif user == "q":
                print("Quitter!")
            else:
                print("INVALID! Please type R ,P, S or Q for quit: ", end="")
                user = "t"

    if computer == 0:
        computerChoice = "Rock"
    elif computer == 1:
        computerChoice = "Paper"
    else: computerChoice = "Scissors"
    print("Your Choice was: ", userChoice)
    print("computer chose: ", computerChoice)


    if userChoice == computerChoice:
        print ("It's a tie!!")
    elif computerChoice == "Paper":
        if userChoice == "Rock":
            print("Computer wins")
            cScore += 1
        else:
            print("You win!!")
            uScore +=1
    elif computerChoice == "Rock":
        if userChoice == "Scissors":
            print("Computer wins")
            cScore += 1
        else:
            print("You win!!")
            uScore += 1
    elif computerChoice == "Scissors":
        if userChoice == "Paper":
            print("Computer wins")
            cScore += 1
        else:
            print("You win!!")
            uScore += 1

    print("You scored: ", uScore, "Computer Scored: ", cScore)
    print("play again?: ", end="")
    play = input()