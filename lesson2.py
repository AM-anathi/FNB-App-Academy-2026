# Tracking individuals letters 
#name = "Python"

# we start counting from 0, so the first letter is at index 0, the second letter is at index 1. 
# print(name[0]) # prints the first letter of the string
# print(name[-1]) # prints the last letter of the string (starting from the right side of the string)
# print(name[2]) # prints the second letter of the string 

#Using the string Methods 

#town = "  Johannesburg  "
#print(town.upper())
#print(town.strip()) # strip() removes the whitespace from the beginning and end of the string 

# Creating a proffesional system email generator 

first = input("Enter your first name : ").strip()
last = input("Enter your last name : ").strip()

username = f" {first[0]}{last}"
print (f" Your email is: {username.lower()}@university.co.za")