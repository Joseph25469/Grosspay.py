#program to print the largest of three numbers


a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if a>b and a>c:
    largest = a
elif b>a and b>c:
    largest= b
else:
    largest= c
    
print("The largest number is:",largest)
    