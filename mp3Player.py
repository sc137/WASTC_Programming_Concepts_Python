# WASTC 2016
# Sable Cantus
#
# start with a list of a fixed size
# fill it with the name of a song
# then shuffle the songs at random
# not really playing songs, just listing them

import random

a = [None for i in range(200)]
n = 0 #size counter

file = open("songs.txt")
for lineFromFile in file: #EOF loop
	aSong = lineFromFile.strip()

	if n < len(a):
		a[n] = aSong
		n += 1

# print (a[:n])

while True:
	playNext = input("Play a song? [Y/N]: ")
	if not playNext.lower() == 'y': break
	
	i = random.randint(0, n -1) # inclusive
	print (a[i])

file.close()