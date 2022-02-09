#program to generate grade


#prompt the user to enter sores for each subject

Maths = int(input("Enter you score in Maths: "))
English = int(input("Enter you score in English: "))
Kiswahili = int(input("Enter you score in Kiswahili: "))
Physics = int(input("Enter you score in Physics: "))
Chemistry = int(input("Enter you score in Chemistry: "))

#calculate the average
score = (Maths+English+Kiswahili+Physics+Chemistry)/5

if score >=70 and score<= 100:
    grade = "A"
elif score >=60 and score<= 69:    
    grade = "B"
elif score >=50 and score<= 59:
    grade = "C"
elif score >=40 and score<= 49:
    grade = "D"
else:
    grade = "FAIL"
    
print("Your score = ",score)
print("Grade = ",grade)
