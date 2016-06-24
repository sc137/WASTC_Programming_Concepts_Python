def factorial(n):
  result = 0
  if n < 2: # detecting a base case
    result = 1
  else:
    result = n * factorial(n - 1) # do this if not base case
  return result
# factorial ends here

# main program starts here
n = int(input("Enter n: "))
print(factorial(n))