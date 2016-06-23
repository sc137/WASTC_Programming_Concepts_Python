import random
mru =[]
class Song:
    name = None
    next = None  # link to next song

start = None  # empty linked list

n = 0
fin = open("songs.txt")  # f in file in but this is optional what your name is
for lineFromFile in fin:  # end of loop
    aSong = lineFromFile.strip()  # strips control characters

    x = Song()
    x.name = aSong
    x.next = start
    start = x  # this is what makes it a linked list this is node one
    n += 1
fin.close()

#this is the list of songs
p = start
while p != None:
    print(p.name)
    p = p.next

    # while true if break favorite loop
while True:
    y = input("Play Song: [Y/N] ")[0]
    if not y.lower() == 'y': break
    while True:
        i = random.randint(0, n - 1)
        found = False
        for j in range(len(mru)):
            if i == mru[j]:
                found = True
                break
        if found: continue
        mru[:0] = [i]  # insert at front
        if len(mru) > 3:
            mru = mru[:len(mru) - 1]  # remove last
        break
    counter = 0
    p = start
    while p != None:
        if counter == i:
            print(p.name, '\n')
            break
        p = p.next
        counter += 1

# while True:
#     i = random.randint(0, n - 1)
#     found = False
#     for j in range(len(mru)):
#         if i == mru[j]:
#             found = True
#             break
#         if found: continue
#         mru[:0] = [i] # insert at front
#         if len(mru) > 3:
#             mru = mru[:len(mru) - 1] # remove last
#         break