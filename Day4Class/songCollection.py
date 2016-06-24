songs = []


# as long as the length of the most recently used que is less than "MAX" then do it
# if it is already at that size then you need to delete stuff

aSong = 'Hey Jude'
songs[:0] = [aSong] # Inserts at the front

aSong = 'She Loves You'
songs[:0] = [aSong] # Inserts at the front

aSong = 'Yellow Submarine'
songs[:0] = [aSong] # Inserts at the front

aSong = 'Imagine'
songs[len(songs):] = [aSong] # Inserts at the end

songs = songs[1:] # removes first song
songs = songs [:len(songs) - 1] # removes last song

print (songs)