a = [None for i in range(5)]
n = 0 # array SIZE (vs CAPACITY)

while True:
  aScore = int(input("Enter a score [0-100, -1 to stop]:"))
  if aScore < 0: break  

  # add to the list
  if n < len(a):
    a[n] = aScore
    n += 1

print(a[:n])