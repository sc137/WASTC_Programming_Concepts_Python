songs = []

aSong = 'Hey Jude'
songs[:0] = [aSong]
print (songs)

aSong = "She Loves You"
songs[len(songs):] = [aSong]

print (songs)