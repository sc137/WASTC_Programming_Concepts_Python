payAmount = int(input("enter how much they owe: "))
tendered = int(input("enter how much they gave you: "))
changeDue = tendered - payAmount

if changeDue > 0:
    print("Cash payment amount: ", payAmount, end="\n")
    print("Tendered amount: ", tendered, end="\n")
    print("Change due: ", changeDue, end="\n")
    print("Change paid out in:", end="\n")

    x = changeDue // 100000
    print("this many hundred thousand dollar bills: ", x, end="\n")
    x = (changeDue % 100000)//10000

    print("this many ten thousand dollar bills: ", x, end="\n")
    x = (changeDue % 10000)//5000

    print("this many five thousand dollar bills: ", x, end="\n")
    x = (changeDue % 5000)//1000

    print("this many thousand dollar bills: ", x, end="\n")
    x = (changeDue % 1000)//500

    print("this many five hundred dollar bills: ", x, end="\n")
    x = (changeDue % 500)//100

    print("this many hundred dollar bills: ", x, end="\n")
    x = (changeDue % 100)//50

    print("this many fifty dollar bills: ", x, end="\n")
    x = (changeDue % 50)//20

    print("this many twenty dollar bills: ", x, end="\n")
    x = (changeDue % 20)//10

    print("this many ten dollar bills: ", x, end="\n")
    x = (changeDue % 10)//5

    print("this many five dollar bills: ", x, end="\n")
    x = (changeDue % 5)//2

    print("this many two dollar bills: ", x, end="\n")
    x = (changeDue % 2)//1

    print("this many one dollar bills: ", x, end="\n")
else:
    x = changeDue * -1
    print("THIEF don't try and bamboozle me. you owe me $",x, " more", sep='')