#a program to check if a number is divisible by both 5 and 7
numb = int(input("enter a number:"))
if numb%5==0 and numb%7==0:
    print(numb,"is divisible by both 5 and 7")
else:
    print(numb,"is not divisible by both 5 and 7")