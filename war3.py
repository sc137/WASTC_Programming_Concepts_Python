# WASTC 2016 Programming Concepts Python
# Sable Cantus
#
# Exercise 7.6 - Game of War v. 3.0
# Would you like to play again?
# must add a variable for each card so it can only be picked once

import random
computerScore = 0
humanScore = 0
play = 'y'

print ("Let's play a game!", "\n")

while play.lower() == 'y':

    #generate cards and suite's
    computerCard = random.randint(2,14)
    computerSuite = random.randint(0,3)
    computerCardFace = computerCard

    humanCard = random.randint(2,14)
    humanSuite = random.randint(0,3)
    humanCardFace = humanCard

    # head-bash approach to naming
    if computerSuite == 0:
        computerSuite = "Spades"
    elif computerSuite == 1:
        computerSuite = "Hearts"
    elif computerSuite == 2:
        computerSuite = "Spades"
    elif computerSuite == 3:
        computerSuite = "Diamonds"

    if computerCard > 10:
        if computerCard == 11:
            computerCardFace = "Jack"
        elif computerCard == 12:
            computerCardFace = "Queen"
        elif computerCard == 13:
            computerCardFace = "King"
        elif computerCard == 14:
            computerCardFace = "Ace"

    if humanSuite == 0:
        humanSuite = "Spades"
    elif humanSuite == 1:
        humanSuite = "Hearts"
    elif humanSuite == 2:
        humanSuite = "Spades"
    elif humanSuite == 3:
        humanSuite = "Diamonds"

    if humanCard > 10:
        if humanCard == 11:
            humanCardFace = "Jack"
        elif humanCard == 12:
            humanCardFace = "Queen"
        elif humanCard == 13:
            humanCardFace = "King"
        elif humanCard == 14:
            humanCardFace = "Ace"

    #pretty output
    print ()
    print ("Computer's card is a", computerCardFace, "of", computerSuite)
    print ("Your card is a", humanCardFace, "of", humanSuite)
    print ()

    # determine the winner
    if computerCard == humanCard:
        print (">>>>> It's a tie! This means WAR <<<<<")
    elif computerCard > humanCard:
        print (">>>>> Computer wins :<()")
        computerScore =+ 1
    else:
        print (">>>>> You win! <<<<<")
        humanScore += 1

    print ()
    print("Computer:", computerScore)
    print("Human: ", humanScore)

    if humanScore == 52:
        print ("You win the game!")
        break
    elif computerScore == 52:
        print ("You lose, computer wins. Better luck next time.")

    print ()
    print ("Would you like to play again? ", end="")
    play = input()[0]