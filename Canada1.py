# WASTC 2016 Programming Concepts Python
# Sable Cantus
#
# Exercise 5.4 - Temperature Conversion
# Convert Celsius to Farenheit

# c = 36
print ("Please enter the degrees in Celsius: ", end="")
c = float(input())
f = ((9 * c) / 5) + 32
# print (f)

print (c, u"\u00b0"," Celsius is ", f, u"\u00b0", " Fahrenheit", sep="")