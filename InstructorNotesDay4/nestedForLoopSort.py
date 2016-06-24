a = [13, 5, 2, 21, 78, 5, 5.5]
b = a.copy()

for i in range(len(a)):
  for j in range(i + 1, len(a)):
    if a[j] < a[i]:
      a[i],a[j] = a[j],a[i]

b.sort()
a[0] = 'A'
b[0] = 'B'
print(a, b, sep='\n')

