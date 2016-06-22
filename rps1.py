# WASTC 2016
# Sable Cantus
# 
# Exercise 7.8, Rock, Paper, Scissors
# http://www.rdb3.com/python/exercises/7.8.pdf

# need to fix "enter" as out of range...

import random, time

# vars
computerScore = 0
player1Score = 0
winner = 0

play = 'y'

print ("Let\'s play a game!")

while play.lower() == 'y':
	#generate computer play
	computerPlay = random.randint(1,3)
	
	# debug
	# print ("debug cheat - computerPlay = ", computerPlay)
	
	if computerPlay == 1:
		computerChoice = 'r'
	if computerPlay == 2:
		computerChoice = 'p'
	if computerPlay == 3:
		computerChoice = 's'

	print ("Choose: [Rock, Paper, Scissors, Quit]: ", end="")
	player1Choice = input()[0]
	player1Choice = player1Choice.lower()	
		
	player1Play = 0
	
	if player1Choice == 'r':
		player1Play = 1
	elif player1Choice == 'p':
		player1Play = 2
	elif player1Choice == 's':
		player1Play = 3
	else:
		break
	time.sleep(0.5)

	# 1 = rock
	# 2 = paper
	# 3 = scissors

	if player1Play == 1 and computerPlay == 1:
		winner = 'Tie!'
	if player1Play == 1 and computerPlay == 2:
		winner = 'Computer wins!'
		computerScore += 1
	if player1Play == 1 and computerPlay == 3:
		winner = 'You win!'
		player1Score += 1	
	
	if player1Play == 2 and computerPlay == 1:
		winner = 'You win!'
		player1Score += 1	
	if player1Play == 2 and computerPlay == 2:
		winner = 'Tie!'
	if player1Play == 2 and computerPlay == 3:
		winner = 'Computer wins!'
		computerScore += 1

	if player1Play == 3 and computerPlay == 1:
		winner = 'Computer wins!'
		computerScore += 1
	if player1Play == 3 and computerPlay == 2:
		winner = 'You win!'
		player1Score += 1
	if player1Play == 3 and computerPlay == 3:
		winner = 'Tie!'
	
	print ("Computer:", computerChoice.upper(), " You:", player1Choice.upper(), " ", winner, sep="")
	print ("You:", player1Score, "Computer:", computerScore)
	print ()
	
# 	computerPlay = 0
# 	player1Play = 0

print ("====================")
print ("Final Score:\n")
print ("     You: ", player1Score)
print ("     Computer: ", computerScore)
print ("==========gg==========")
