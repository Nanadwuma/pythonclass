'''
write a code that grades students where 
above 80 is grade A
70-79 = B
60-69 =C
50-59 = D
30-49= F (Tell stdent to resit )
below 30 is Repeat Class
'''

'''print("Enter Marks Obtained in 5 Subjects: ")
mark_one = int(input())
mark_two = int(input())
mark_three = int(input())
mark_four = int(input())
mark_five = int(input())

total = mark_one + mark_two + mark_three + mark_four + mark_five
average = total/5
if average>=80 and average <=100 :
    print("Your Grade is A")
elif average>=70 and average<79 :
    print("Your Grade is B")
elif average>=60 and average<69 :
    print("Ypur Grade is C")
elif average>=50 and average<59 :
    print("Ypur Grade is D")
elif average>=40 and average<49 :
    print("Ypur Grade is E")
elif average>=0 and average<39 :
    print("Your Grade is F. You are to resit.")
else:
    print("Repeat Class!") '''

'''
grade = float(input("What was your score?"))

if grade >=90 and grade <=100:
    print("Your grade is A")
elif grade >=80 and grade <=89:
    print("Your grade is B")
elif grade >=70 and grade <=79:
    print("Your grade is C")
else:
    print("Unknown grade")
'''
print("What is your score?")
grade = int(input())

if grade >=80 and grade <=100:
    print("Your grade is A.")
elif grade >=70 and grade <=79:
    print("Your grade is B.")
elif grade >=60 and grade <=69:
    print("Your grade is C.")
elif grade >=50 and grade <=59:
    print("Your grade is D.")
elif grade >=40 and grade <=49:
    print("Your grade is E, you have to resit")
elif grade >=0 and grade <=39:
    print("Your grade is F. Your are to Repeat Class")
else:
    print("Invalid")

