def countDown(n):
  print(n, end="\n")
  if n > 0:
    countDown(n -1)

n = int(input("Enter n: "))
countDown(n)
