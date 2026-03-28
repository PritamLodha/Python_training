currencies = {
    '1': 'INR',
    '2': 'USD',
    '3': 'EUR'
}

incur = input("Choose input currency (1-INR, 2-USD, 3-EUR): ")
oucur = input("Choose output currency (1-INR, 2-USD, 3-EUR): ")

cur = float(input("Enter amount: "))

incur = currencies.get(incur)
oucur = currencies.get(oucur)

rates = {
    ('INR', 'USD'): 0.012,
    ('INR', 'EUR'): 0.011,
    ('USD', 'INR'): 82.87,
    ('USD', 'EUR'): 0.91,
    ('EUR', 'INR'): 90.95,
    ('EUR', 'USD'): 1.10
}

if incur == oucur:
    print(cur)
elif (incur, oucur) in rates:
    print(cur * rates[(incur, oucur)])
else:
    print("Invalid choice")