# WASTC 2016 Programming Concepts Python
# Sable Cantus
#
# Exercise 7.4 - Coin Toss, v. 2.0

import random

i = 0

print ("How many coins shall we toss today? Enter a number: ", end="")
flips = int(input())

while i < flips:
    toss = random.randint(1, 2)
    if toss == 1:
        print ("Heads")
    else:
        print ("Tails")
    i += 1
