a = [None for i in range(10)]
a[3:6] = ("Hi", 3.14159, 12345)

found = False
for i in range(len(a)):
  if a[i] == 12345:
    found = True
    break

if found: print("found it at", i)
else: print("not there")