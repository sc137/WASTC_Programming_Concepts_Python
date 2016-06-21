# Day 1 Exercise - Change Due
# WASTC 6/20/16
# Sable Cantus

amountDue = 273
amountTendered = 300
changeDue = amountTendered - amountDue

if amountTendered < amountDue or amountTendered <= 0:
    print ('The tendered amount is too small. Please pay more than $',amountDue)
else:          
    print('Amount due:', amountDue)
    print('Tendered amount: ', amountTendered)
    print('Change due: ', changeDue)

    hundredThousands = changeDue / 100000
    hundredThousands = int(hundredThousands)
    changeDue = changeDue % 100000

    tenThousands = changeDue / 10000
    tenThousands = int(tenThousands)
    changeDue = changeDue % 10000

    fiveThousands = changeDue / 5000
    fiveThousands = int(fiveThousands)
    changeDue = changeDue % 5000

    oneThousands = changeDue / 1000
    oneThousands = int(oneThousands)
    changeDue = changeDue % 1000

    fiveHundreds = changeDue / 500
    fiveHundreds = int(fiveHundreds)
    changeDue = changeDue % 500

    oneHundreds = changeDue / 100
    oneHundreds = int(oneHundreds)
    changeDue = changeDue % 100

    fifties = changeDue / 50
    fifties = int(fifties)
    changeDue = changeDue % 50

    twenties = changeDue / 20
    twenties = int(twenties)
    changeDue = changeDue % 20

    tens = changeDue / 10
    tens = int(tens)
    changeDue = changeDue % 10

    fives = changeDue / 5
    fives = int(fives)
    changeDue = changeDue % 5

    ones = changeDue / 1
    ones = int(ones)
    changeDue = changeDue % 1

    print ('Change paid out in: ')
    print ('    this many hundred thousand dollar bills: ', hundredThousands)
    print ('    this many ten thousand dollar bills: ', tenThousands)
    print ('    this many five thousand dollar bills: ', fiveThousands)
    print ('    this many thousand dollar bills: ', oneThousands)
    print ('    this many five hundred dollar bills: ', fiveHundreds)
    print ('    this many one hundred dollar bills: ', oneHundreds)
    print ('    this many fifty dollar bills: ', fifties)
    print ('    this many twenty dollar bills: ', twenties)
    print ('    this many ten dollar bills: ', tens)
    print ('    this many five dollar bills: ', fives)
    print ('    this many one dollar bills: ', ones)
