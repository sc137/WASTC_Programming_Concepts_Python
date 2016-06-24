a = [None for i in range(100)]
n = 0 # size counter

fin = open("songs.txt")
for lineFromFile in fin: # EOF loop
  aSong = lineFromFile.strip()
  print(aSong)

fin.close()