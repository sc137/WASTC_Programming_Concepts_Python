def ask(q,a1,a2):
    print(q)
    x = input()
    if x.upper() == a1.upper():
        print("correct")
    elif a2 != None and x.upper () == a2.upper():
        print("Correct")
    else:
        print("Wrong!")

ask("Who invented the internet?", "Al Gore", "Gore")
ask("When was the internet invented?", "1995", None)