# student grade classifier

#learner's name + marks for three subjects

name= input("Enter your name: ")


mark1 = float(input("Enter mark for Subject 1: "))
mark2= float(input("Enter mark for Subject 2: "))
mark3= float(input("Enter mark for Subject 3: "))

#calculate the average 
subject_average = (mark1 + mark2 + mark3)/3 
#assign grade and status (Pass/Fail)
if subject_average >= 80:
   grade = "A" 
   status = "Pass"

elif subject_average >=70 :
    grade = "B"
    status ="Pass"

elif subject_average >= 60 :
    grade = "C" 
    status ="Pass"
elif subject_average >=50 :
    grade = "D"
    status = "Pass"

else: 
    grade ="F"
    status = "Fail"


print("=== Report Card ===")
print(f"Student Name: {name}")
print(f"Subject 1: {mark1}")
print(f"Subject 2: {mark2}")
print(f"Subject 3: {mark3}")
print(f"Average: {round(subject_average,2)}")
print(f"Grade: {grade}")
print(f"Status: {status}")
#subject intervention below 40

if mark1 < 40:
    print("Subject 1: needs intervention ")
if mark2 < 40:
    print("Subject 2: needs intervention ")
if mark3 < 40:
    print("Subject 3: needs intervention ")

print("========================")






