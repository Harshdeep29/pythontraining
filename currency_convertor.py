incur=input('''Choose the input currency:
            1. INR
            2. USD
            3. EUR''')
oucur=input('''Choose the output currency:
            1. INR
            2. USD
            3. EUR''')
cur=float(input("Enter the amount: "))
if incur=='INR':
    if oucur=='INR':
        print(cur)
    if oucur=='USD':
        print(cur*0.012)
    if oucur=='EUR':
        print(cur*0.011)
elif incur=='USD':
    if oucur=='INR':
        print(cur*82.87)
    if oucur=='USD':
        print(cur)
    if oucur=='EUR':
        print(cur*0.91)
elif incur=='EUR':
    if oucur=='INR':
        print(cur*90.95)
    if oucur=='USD':
        print(cur*1.10)
    if oucur=='EUR':
        print(cur)
else:
    print("Choose the given choice only :)")

