#program to calculate Discount
amount = float(input("Enter amount: "))
if amount>1000:
    discount = 0.05*amount
    print("Discount = sh",discount)
else:
    print("No discount")