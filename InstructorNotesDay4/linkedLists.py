class Song:
  name = None
  next = None # link to next song

start = None # empty linked list

x = Song()
x.name = 'Hey Jude'
x.next = start # put here to match below
start = x

x = Song()
x.name = 'Yellow Sub'
x.next = start # insert at start...
start = x      # ...of the list

x = Song()
x.name = 'Imagine'
x.next = start # insert at start...
start = x      # ...of the list

p = start
while True:
  if p == None: break
  print(p.name)
  p = p.next


