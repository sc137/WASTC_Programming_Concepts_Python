# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    i = n
    while i > 1:
        i = i -1
        n = n * i
    if n == 0:
        n = 1
    return n

# #example from prof
# def factorial(n):
#         result = 1
#         while n >= 1:
#             result = result * n
#             n = n -1
#         return result

print (factorial(8))
