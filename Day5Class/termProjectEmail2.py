def isValid(c):
    if ('0' <= c and c <= '9' ): return True
    if ('A' <= c and c <= 'Z'): return True
    if ('a' <= c and c <= 'z'): return True
    if (c in ".!#$%&'*+-/=?^_`{|}~"): return True
    return False

a = [None for i in range(1000)]
n = 0

fin = open('/Users/danaarazi/gitShit/WASTC_Programming_Concepts_Python/Day3Class/sample_email_lists.txt')
for line in fin:
    for i in range(len(line)):
      if (line[i] == '@'):
        hasDot = False
        for s in range(i - 1, -1, -1):
          if not isValid(line[s]):
            break
        if not isValid(line[s]): s += 1
        for e in range(i + 1, len(line)):
          if not isValid(line[e]):
            break
          if line[e] == '.': hasDot = True
        if isValid(line[e]): e += 1
        if s < i and i < e and hasDot:
            found =  False
            for j in range (n):
                if line[s:e] == a[j]:
                    found = True
            if not found:
                if n < len(a):
                    a[n] = line[s:e]
                n += 1
                #print(line[s:e], end="\n")

fin.close()

a = a[:n] #this clips the array to remove unused capacity

#a.sort() #this sort function seperates upper and lower case.
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[j].upper() < a[i].upper():
            a[i], a[j] = a[j], a[i]


for i in range(len(a)):
    print (a[i])
    i += 1

fout = open("formattedEmail.txt", 'w')
for i in range(len(a)):
    fout.write(a[i] + '\n')  # this one is for a list on seperate lines
    #fout.write(a[i])  #this one is for a ; seperated list
    #if i < len(a): fout.write(';') #this one is for a ; seperated list
    i += 1