a = [None for i in range(10)]
a[3] = 'hi'
a[4] = 3.14159
a[5] = 12345
b = a + []
b[0] = "B"
a[3] = (3,4,5)
#a[3:6] = (3,4,5)
a = "one two three four five"
a=a.split(' ')

print(b)
print(a)

#SEARCHES
found = False
for i in range(len(b)):
    if b[i] == 12345:
        found = True
        break

if found: print("found it at: ", i)
else: print("not found")