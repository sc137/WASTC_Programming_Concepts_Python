class Song:
  name = None
  next = None # link to next song

start = None # empty linked list

n = 0
fin = open("songs.txt")
for lineFromFile in fin: # EOF loop
  aSong = lineFromFile.strip()

  x = Song()
  x.name = aSong
  x.next = start # put here to match below
  start = x
  n += 1

fin.close()

# list of songs
p = start
while p != None:
  print(p.name)
  p = p.next

# user interface
import random
while True:
  answer = input("Play? [Y/N]")[0].upper()
  if answer == 'N': break

  i = random.randint(0, n - 1) # inclusive
  
  counter = 0
  p = start
  while p != None:
    if counter == i:
      print(p.name)
      break
    p = p.next
    counter += 1

