print("Enter borrowed amount:", end='')
p = int(input())
print("entered annual APR rate%:", end='')
i = float(input())


r = i / 12 / 100
n = 30 * 12

x = (1 + r)**n
mp = (p * x * r) / (x-1)
mpFormatted = "%.2f" % mp
totalPayments = mp * n
totalPaymentsFormatted = "%.2f" % totalPayments
print("Your Monthly payment is: ", mpFormatted)
print("Your Monthly payment is: ", totalPaymentsFormatted)
