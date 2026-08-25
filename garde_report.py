#unit 6 Practical Task
#5 students 
students = [
    {"name": "Anna", "Maths": 80, "English": 75, "Science": 86},
    {"name": "Nthando", "Maths": 90, "English": 65, "Science": 63},
    {"name": "Thembi","Maths": 35, "English": 76, "Science": 54},
    {"name": "Lerato","Maths": 47, "English": 86, "Science": 34},
    {"name": "Emilia", "Maths": 25, "English": 87, "Science": 33},
    
]
results = []


# calculate each students average 
for student in students :
    average = (student["Maths"] + student["English"] + student["Science"]) /3

#grade/status logic from unit 5
    if average >= 80:
     grade = "A" 
     status = "Pass"

    elif average >=70 :
     grade = "B"
     status ="Pass"

    elif average >= 60 :
     grade = "C" 
     status ="Pass"

    elif average >=50 :
     grade = "D"
     status = "Pass"

    else: 
     grade ="F"
     status = "Fail"
 
    results.append( {
     "name": student["name"],
     "average": round(average,2),
     "grade": grade, 
     "status":status
})
# calculate class average

class_average = sum([result["average"] for result in results]) / len(results)
print(f"Class Average:{round(class_average,2)}")

for result in results:
 print("=== Report Card ===")
 print(f"Student Name: {result['name']}")
 print(f"Average: {result['average']}")
 print(f"Grade: {result['grade']}")
 print(f"Status: {result['status']}")
 print("========================")
# user search for a student by name after the report is shown 
while True: 
  search_name =input ("Enter a students name to search for (or type 'exit' to quit):") 
  if search_name.lower() == "exit":
    break 
  else:
    found_student =None #None is a special value in python that represents the absence of a value or a null value
    for result in results:
      if result['name'].lower() == search_name.lower():
        found_student = result
        break

    if found_student:
      print(f"Student Name: {found_student['name']}")
      print(f"Average: {round(found_student['average'],2)}")
      print(f"Grade: {found_student['grade']}")
      print(f"Status: {found_student['status']}")
      print("========================")
    else:
      print("Student not found.")
