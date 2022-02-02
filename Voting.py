#program to check if a person is eligible to vote\
age = int(input("Enter age:"))
nationality = input("Enter nationality: ").lower()

if age>=18 and nationality=="kenyan":
    print("Eligible to vote")
else:
    print("You are not eligible to vote")