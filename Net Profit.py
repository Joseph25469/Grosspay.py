#program to calculate the net bonus amount in a company


step1:prompt the user to enter their salary and years of service

step2:if period of service >10 years- bonus= 10%

setp3:if period of service >1=6 and <=10 years- bonus= 8%

step4:if period of service <6 years- bonus= 5%

step5: print the net bonut amount 








#prompt the user to enter their salary and years of service

salary = float(input("Enter the salary: "))
years_of_service = int(input("Enter years of service: "))


if years_of_service>10:
    net_bonus = salary*0.10
    print("net bonus =",net_bonus)
elif years_of_service>=6 and years_of_service<=10:
    net_bonus = salary*0.08
    print("net bonus",net_bonus)
elif years_of_service<6:
    net_bonus = salary*0.05
    print("net bonus",net_bonus)
    