class Song:
    name = None
    next = None # link to next song

start = None #empty linked list

x = Song()
x.name = 'Hey Jude'
next = start
start = x # this is what makes it a linked list this is node one

x = Song()
x.name = 'Yellow Submarine'
x.next = start
start = x

x = Song()
x.name = 'Imagine'
x.next = start
start = x

# while true if break favorite loop
p = start
while True:
    if p == None: break
    print(p.name)
    p=p.next
