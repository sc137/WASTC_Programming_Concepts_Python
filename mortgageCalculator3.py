# WASTC 2016 Programming Concepts Python
# Sable Cantus
#
# Exercise 5.1 - Mortgage Calculator
# adding user input

#p = 800000
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

print("==========")
print ("Amount borrowed is $", p, sep="")
print ("Term length is", y,'years')
print ("APR is ", i, "%", sep="")
print ("Monthly payment is ", "$", mpFormatted, sep="")
print ("Total cost over ",y," years is $", tcFormatted, sep="")