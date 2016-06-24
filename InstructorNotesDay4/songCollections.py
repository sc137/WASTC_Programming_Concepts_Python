songs = []

aSong = "Hey Jude"
songs[:0] = [aSong] #insert at front

aSong = "She Loves You"
songs[:0] = [aSong] #insert at front

aSong = "Imagine"
songs[:0] = [aSong] #insert at front

aSong = "Yellow Sub"
songs[len(songs):] = [aSong] #insert at front

songs = songs[1:] # remove first song
songs = songs[:len(songs) - 1] # remove last

print(songs)