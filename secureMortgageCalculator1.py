# WASTC 2016
# Sable Cantus
# 
# Exercise 8.3, Password-protected mortgage Calculator
# http://www.rdb3.com/python/exercises/8.3.pdf

def mortgageCalculator():
	print ("Enter borrowed amount: ", end='')
	p = int(input())
	
	print ("How many years is the term? ", end="")
	y = int(input())
	
	print ("Enter annual rate%: ", end='')
	i = float(input())
	
	r = i / 12 / 100
	n = y * 12
	
	x = (1 + r)**n
	mp = (p * x * r) / (x - 1)
	mpFormatted = "%.2f" % mp
	
	totalCost = mp * (y * 12)
	tcFormatted = "%.2f" % totalCost
	
	print("====================")
	print ("Amount borrowed is $", p, sep="")
	print ("Term length is", y,'years')
	print ("APR is ", i, "%", sep="")
	print ("Monthly payment is ", "$", mpFormatted, sep="")
	print ("Total cost over ",y," years is $", tcFormatted, sep="")
	print("====================")
# end function #

password = "sierra mist"
pwd = None

# first request a password for access
# we'll limit tries next attempt

while True:
	print ("Please enter your password: ", end="")
	pwd = input()
	if pwd == password:         # get it right, come on in
		mortgageCalculator()
		break
	else:
		print ("INVALID")