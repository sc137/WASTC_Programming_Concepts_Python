# WASTC 2016 Programming Concepts Python
# Sable Cantus


while True:
    print ("Enter your grade [A,B,C,D,F]: ", end='')
    x = input()[0]

    if x.lower() == 'a' or x.lower() == 'b' or x.lower() == 'c':
        print ("You passed!")
        break

    elif x.lower() == 'd' or x.lower() == 'f':
        print ("You did not pass!")
        break

    else:
        print ("Please enter a grade letter [A,B,C,D,F].")