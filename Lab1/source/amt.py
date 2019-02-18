
Totalamt = 0

while True:
    str = input()
    if not str:
        break

    values = str.split(" ")
    trans = values[0]
    amt = int(values[1])

    if trans == 'Deposit':
        Totalamt += amt
    elif trans == 'Withdraw':
        Totalamt -= amt

print(" Total Amount -", Totalamt)
