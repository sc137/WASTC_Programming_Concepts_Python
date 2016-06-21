# WASTC 2016 Programming Concepts Python
# Sable Cantus
#
# Exercise 6.2 - Input Validation

i = 0
password = "Rubber Bumpers"     # just for testing

while i < 3:                    # only three attempts
    print ("Please enter your password: ", end="")
    pwd = input()

    if pwd == password:         # get it right, come on in
        print ("Welcome to Mazanon.com! Here is your account info...")
        break
    else:                       # uh oh, errors abound
        tries = 2 - i
        if tries > 1:
            print ("You have", tries,"attempts left.")
        elif tries == 1:
            print ("Last attempt.")
        i += 1

if i >= 3:                      # now you are screwed
    print ("Too many attempts. Your password has been reset. Please contact the helpdesk.")