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
mru = []
while True:
  answer = input("Play a song? [Y/N]")[0].upper()
  if answer == 'N': break

  while True:
    i = random.randint(0, n - 1) # inclusive

    # see if this MRU'd
    found = False
    for j in range(len(mru)):
      if i == mru[j]:
        found = True
        break
    if found: continue # if so, get another "i"

    # ok, "i" is good -- remember it in MRU
    mru[:0] = [i] # insert at front
    if len(mru) > 3: 
      mru = mru[:len(mru) - 1] # remove last
    break
      
  print(a[i]) # play the song