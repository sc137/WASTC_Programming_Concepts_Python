# WASTC 2016 Programming Concepts Python
# Sable Cantus
#
# Exercise 5.1 - Mortgage Calculator

p = 800000
r = 3.99 / 12 / 100
n = 30 * 12

x = (1 + r)**n
mp = (p * x * r) / (x - 1)
mpFormatted = "%.2f" % mp

print("Monthly payment is ", "$", mpFormatted, sep="")