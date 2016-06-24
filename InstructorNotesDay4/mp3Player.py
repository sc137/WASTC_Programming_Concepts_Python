a = [None for i in range(100)]
n = 0 # size counter

fin = open("songs.txt")
for lineFromFile in fin: # EOF loop
  aSong = lineFromFile.strip()

  if n < len(a):
    a[n] = aSong
    n += 1
  
fin.close()

import random
while True:
  answer = input("Play a song? [Y/N]")[0].upper()
  if answer == 'N': break

  i = random.randint(0, n - 1) # inclusive
  print(a[i])