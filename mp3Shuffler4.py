# WASTC 2016
# Sable Cantus

import random
class Song:
    name = None
    next = None     				# link to next song obj.
start = None        				# creates empty linked list

n = 0               				# size counter
# get songs from a file
file = open("songs.txt")
for lineFromFile in file: 			#EOF loop
    aSong = lineFromFile.strip()
    x = Song()
    x.name = aSong
    x.next = start
    start = x
    n +=1
file.close()

# track recently played
recent = [None for i in range(3)]

while True:
	# generate a random number to pick a song
	while True:
		i = random.randint(0, n -1)
		found = False
		# see if in recents, if so get another i
		if i in recents:
			found = True
			break
		if found: continue
	
	#ask the user for input
	playNext = input("Play a song? [Y/N]: ")
	if not playNext.lower() == 'y':
		break

	counter = 0
	p = start
	while p != None:
		if counter == i:
			print(p.name)
			break
			recent[:0] = [p.name]
			recent[3].pop()
		p = p.next
		counter += 1
		
print (recent)
