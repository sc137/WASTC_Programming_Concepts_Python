a = [None for i in range(4)]

total = 0
for i in range(len(a)):
  a[i] = int(input("Enter a value:"))
  total += a[i]
average = total / len(a)
print("The average is", average)

nGreater = 0
for i in range(len(a)):
  if a[i] > average: nGreater += 1
print("# greater than average is", nGreater)