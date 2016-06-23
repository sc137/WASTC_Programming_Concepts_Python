a = [1,2,3,9,7,4,6,7,2,8]
a[4] = 3.14159
a[5] = 12345
b = a + []
b[0] = 100
#a[3:6] = (3,4,5)


#print(b)
#print(a)

#SEARCHES
found = False
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[j] < a[i]:
            a[i],a[j] = a[j],a[i]
b.sort()

print(a, b, sep='\n')

a.sort(reverse=True)
print(a)