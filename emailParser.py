# email parser
def isValid(c): # check for valid email chars
  if ('0' <= c and c <= '9'): return True
  if ('A' <= c and c <= 'Z'): return True
  if ('a' <= c and c <= 'z'): return True
  if ('.' == c or c == '-'): return True
  #if ('_' == c): return True
  return False

# array-based list for storing up to 1000 emails
a = [None for i in range(1000)]
n = 0 # array SIZE (vs CAPACITY)

# parse a file
fin = open("emails.txt")
for line in fin: # EOF loop

  # look for @ in the line
  for i in range(len(line)):
    if (line[i] == '@'):

      # look left and right for beginning and end of candidate email
      hasDot = False
      for s in range(i - 1, -1, -1):
        if not isValid(line[s]):
          break
      if not isValid(line[s]): s += 1 # in case we run past the start of line
      for e in range(i + 1, len(line)):
        if not isValid(line[e]):
          break
        if line[e] == '.': hasDot = True
      if isValid(line[e]): e += 1 # in case we run out the end of line

      # the candidate is a valid address
      if s < i and i < e and hasDot:

        # see if it's already in the list
        found = False
        for j in range(n):
          if line[s:e].upper() == a[j].upper():
            found = True

        # if not, add it to the list
        if not found:
          if n < len(a):
            a[n] = line[s:e]
            n += 1

fin.close()

a = a[:n] # clip the array -- lose unused capacity
a.sort() # sort (case DEPENDENT -- fix later)
print(a) # unformatted list...







