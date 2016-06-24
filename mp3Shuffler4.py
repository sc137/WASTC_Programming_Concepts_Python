# WASTC 2016
# Sable Cantus

import random
songs = [None for i in range(100)]
n = 0               				# size counter

# get songs from a file
file = open("songs.txt")
for lineFromFile in file: 			#EOF loop
    aSong = lineFromFile.strip()
    
    if n < len(songs):
    	songs[n]=aSong
    	n += 1
file.close()

# track recently played
recent = []
while True:
	#ask the user for input
	playNext = input("Play a song? [Y/N]: ")
	if not playNext[0].lower() == 'y':
		break
		
	while True:
		i = random.randint(0, n -1)
		
		found = False
		# see if in recents, if so get another i
		for j in range(len(recent)):
			if i == recent[j]:
				found = True
				break
		if found: continue

		recent[:0] = [i]
		if len(recent) > 3:
			recent = recent[:len(recent) -1]
		break
	
	print (songs[i])
		
print (recent)
print (songs[:n])
