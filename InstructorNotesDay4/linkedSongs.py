class Song:
  name = None
  next = None # link to next song

start = None # empty linked list

fin = open("songs.txt")
for lineFromFile in fin: # EOF loop
  aSong = lineFromFile.strip()

  x = Song()
  x.name = aSong
  x.next = start # put here to match below
  start = x

fin.close()

p = start
while p != None:
  print(p.name)
  p = p.next


