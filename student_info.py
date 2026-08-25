# Student information 
# data types: string, integer, float
name = input("Enter your firstname : ")
surname = input("Enter your surname : ")
full_name = name + " " + surname 

# displaying the name in uppercase and in title case 

full_name_upper = full_name.upper()  # upper() converts the string to uppercase
print(full_name_upper)

full_name_title = full_name.title() # title() converts the string to title case
print(full_name_title)


age = int (input ("Enter your age:"))
# Calculating age in months 
age_in_months = age *12
print(age_in_months)


favorite_number= float(input("Enter your favorite number (e.g. 3.14):"))
#Round favorite number to 2 decimal places 
favorite_number_rounded = round(favorite_number, 2) # round() rounds the number to the specified number of decimal places 
 
# greeting the user
print( f" Welcome, {full_name}!") 

#print using type()
full_name_type = type(full_name)
print(full_name_type)
full_name_upper_type = type(full_name_upper)
print(full_name_upper_type)
full_name_title_type = type(full_name_title)
print(full_name_title_type)
age_in_months_type = type(age_in_months)
print(age_in_months_type)
favorite_number_rounded_type = type(favorite_number_rounded)
print(favorite_number_rounded_type)
