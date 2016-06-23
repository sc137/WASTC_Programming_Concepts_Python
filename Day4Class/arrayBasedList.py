a = [None for i in range(5)]



n = 0 # array size NOT capacity (that is 5)

while True:
    aScore = int(input("Enter a Score[0-100]"))
    if aScore < 0: break
    # add to the list (if there is room)
    if n < len(a):
        a[n] = aScore
        n += 1
print(a)
