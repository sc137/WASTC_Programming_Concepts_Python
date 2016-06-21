# WASTC 2016 Programming Concepts demo
# Sable Cantus

# print("Guess my # [1-10]: ", end="")
# x = int(input())
#
# if x == 7:
#     print ("You guessed it!")
# else:
#     print ("Not yet, try again.")

import random

#randomize n on each run
n = random.randint(1,10)
print ("Cheat code - the answer is", n)

while True:
    print ("I'm thinking of a number between one and ten. Guess my # [1-10]: ", end="")
    x = int(input())

    if x > 10:
        print ("Too high! My number is between one and ten.")

    elif x !=n:
        print ("It's not", x, "- Keep trying...")

    if x == n:
        print ("You guessed it! The number I was thinking of was", n)
        break

print ("Thanks for playing :-)")