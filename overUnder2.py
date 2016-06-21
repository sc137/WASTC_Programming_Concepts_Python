# WASTC 2016 Programming Concepts demo
# Sable Cantus
#
# Exercise 6.7 - Over Under v. 2

import random

# pick a random number between 1 and 100
n = random.randint(1,100)

print ("Cheat code - the answer is", n)

while True:
    print ("I'm thinking of a number between one and one hundred. Guess my # [1-100]: ", end="")
    x = int(input())

    if x == n:
        print()
        print ("===== You guessed it! The number I was thinking of was", n,"=====")
        break

    if x > n:
        print ("Too high...")

    if x < n:
        print ("Too low...")



print ("Thanks for playing :-)")