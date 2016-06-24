
def isValid(c):
    if ('0' <= c and c <= '9' ): return True
    if ('A' <= c and c <= 'Z'): return True
    if ('a' <= c and c <= 'z'): return True
    if (c in ".!#$%&'*+-/=?^_`{|}~"): return True
    return False


# p will be an array item with potential emails
def isEmail(p):
    if not ('..'in p):
        print("this has double'..'")
        return True # I am trying to check for double ..
    if not ('@@' in p):
        print("this has double @@")
        return True
    return False # I am trying to check for double @@

potentialEmail = []

#line = "<dana@dansid..com>  george martin@youremail.com"
for i in range(len(line)):
    if(line[i] == '@'):
        hasDot = False
        email = False
        for s in range (i -1, -1, -1):
            if not isValid(line[s]):
                break
        if not isValid(line[s]): s += 1
        for e in range(i + 1, len(line)):
            if not isValid(line[e]):
                break
            if line[e] == '.': hasDot= True
        if isValid(line[e]): e += 1
        if isEmail(line):
            email = True
            break

        print(s, e, hasDot, email, line[s:e])
        potentialEmail.append(line[s:e])


# need another function to remember where the last place of 'e' was in the above
# function then start the search from that section
# need another function that will go through line by line
# perhaps a while loop. not sure how to know when to stop or if it just knows
# the text is done



