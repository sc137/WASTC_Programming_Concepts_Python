# WASTC 2016
# Sable Cantus
#
# Project 15.3 - MP3 Shuffler 2
# http://www.rdb3.com/python/exercises/15.3.pdf
import random

a = [None for i in range(200)]
n = 0 #size counter

file = open("songs.txt")
for lineFromFile in file: #EOF loop
	aSong = lineFromFile.strip()

	if n < len(a):
		a[n] = aSong
		n += 1
file.close()

# print (a[:n])

while True:
	playNext = input("Play a song? [Y/N]: ")
	if not playNext.lower() == 'y': break
	
	i = random.randint(0, n -1) # inclusive
	print (a[i])