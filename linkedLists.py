# WASTC 2016
# Sable Cantus

class Song:
    name = None
    next = None     # link to next song obj.

start = None        # creates empty linked list

x = Song()
x.name = 'Hey Jude'
x.next = start      # these lines allow us to insert
start = x           # records at start of the list

x = Song()
x.name = 'Yellow Submarine'
x.next = start
start = x

x = Song()
x.name = 'Sgt. Peppers'
x.next = start
start = x

# traverse the list
p = start
while p != None:
    print (p.name)
    p = p.next
    
    
'''
n = 0 #size counter

file = open("songs.txt")
for lineFromFile in file: #EOF loop
	aSong = lineFromFile.strip()

	if n < len(a):
		a[n] = aSong
		n += 1
file.close()
'''