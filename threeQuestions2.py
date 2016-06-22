# WASTC 2016
# Sable Cantus
# 
# Exercise 8.5 - Three Quesion Quiz, v. 2.0
# http://www.rdb3.com/python/exercises/8.5.pdf

# 1. Who invented computers?
# ...the first computer resembling today's
# modern machines was the Analytical Engine,
# a device conceived and designed by British
# mathematician Charles Babbage between 1833 and 1871

# 2. When were computers invented?

# 3. How many computer languages are there?
# lots

correct = 0
asked = 0

def askQuestion(q, a1, a2):
	print(q, end="")
	answer = input()
	if answer.lower() == a1.lower() :
		print ("Correct")
		return True
	elif a2 != None and answer.lower() == a2.lower(): 
		print ("Correct")
		return True
	else: 
		print ("Wrong")
		return False
		
asked += 1
if askQuestion("1. Who invented computers? ", "Charles Babbage", "Babbage") : correct += 1

asked += 1
if askQuestion("2. When were computers invented? ", "1946", "1943") : correct += 1

asked += 1
if askQuestion("3. How many computer languages are there? ", "lots", "lots") : correct += 1

print ("You got", correct,"out of", asked,"correct.")

