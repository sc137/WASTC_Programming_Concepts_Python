# WASTC 2016
# Sable Cantus

# a = [0 for i in range(10)]
# print (a)
# 
# a = [None for i in range(10)]
# print (a)
# 
# a = [None for i in range(10)]
# a[0] = 'R'
# a[1] = 'O'
# a[2] = 'Y'
# a[3] = 'G'
# a[4] = 'B'
# a[5] = 'I'
# a[6] = 'V'
# a.pop(7)
# a.pop(7)
# a.pop(7)
# print (a[1:5])


# a = [None for i in range(10)]
# a[3] = (5,5,5)
# print(a)

# a = ['one','two','three','four','five','one']
# for i in range(len(a)):
#     if a[i] == 'one':
#             print ('found at ', i)
#             found = True

a = [5,7,3,2,1,6**3,4,5/2]
for i in range(len(a)):
	for j in range(i + 1, len(a)):
		if a[j] < a[i]:
			a[i],a[j] = a[j],a[i]

print(a)
