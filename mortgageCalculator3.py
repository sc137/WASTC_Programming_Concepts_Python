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

# r = rate
r = i / 12 / 100

# n = number of months for term
n = y * 12

# x = 
x = (1 + r)**n

# mp = monthly payment
mp = (p * x * r) / (x - 1)
mpFormatted = "%.2f" % mp


totalCost = mp * (y * 12)
tcFormatted = "%.2f" % totalCost
interestPaid = totalCost - p
ipFormatted = "%.2f" % interestPaid

print ("==========")
print ("Amount borrowed is $", p, sep="")
print ("Term length is", y,'years')
print ("APR is ", i, "%", sep="")
print ("Monthly payment is ", "$", mpFormatted, sep="")
print ("Total cost over ",y," years is $", tcFormatted, sep="")
print ("Interest paid is $", ipFormatted, sep="")
