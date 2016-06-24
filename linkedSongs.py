# WASTC 2016
# Sable Cantus

class Song:
    name = None
    next = None     # link to next song obj.
start = None        # creates empty linked list

file = open("songs.txt")
for lineFromFile in file: #EOF loop
    aSong = lineFromFile.strip()
    x = Song()
    x.name = aSong
    x.next = start
    start = x
file.close()

# traverse the list
p = start
while p != None:
    print (p.name)
    p = p.next
    



