#membership operators (in)
country = ["kenya", "uganda","tanzania"]
nationality = input("Enter country: ").lower()
age = int(input("Enter age: "))
if nationality in country and age>18:
    print("You are Eligible to vote")
else:
    print("Not eligible to vote")