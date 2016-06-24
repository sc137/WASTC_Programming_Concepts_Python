# WASTC 2016
# Sable Cantus

import random
class Song:
    name = None
    next = None     # link to next song obj.
start = None        # creates empty linked list

n = 0               # size counter

file = open("songs.txt")
for lineFromFile in file: #EOF loop
    aSong = lineFromFile.strip()
    x = Song()
    x.name = aSong
    x.next = start
    start = x
    n +=1
file.close()

recent = [None for i in range(3)]

while True:
    playNext = input("Play a song? [Y/N]: ")
    if not playNext.lower() == 'y':
        break
    
    i = random.randint(0, n -1)
    
    counter = 0
    p = start
    while p != None:
    	if counter == i:
    		print(p.name)
    		break
    	p = p.next
    	counter += 1

# print (recent)
