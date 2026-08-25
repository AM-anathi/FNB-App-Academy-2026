# Username and Message Formatter

# Collecting first name, last name and bio message 

first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()

#Username 

username = f"{first[0]}{last}"
print(f"Your username is: {username.lower()}")

#Ful name in Title Case
full_name = first + " "+ last
full_name_title = full_name.title()
print(full_name_title)


bio = input("Write a bio message: ").strip()
# Count and display the number in the bio 

bio_length = len(bio) # this counts the number of characters in the bio message
print(f"Your bio message is {bio_length} characters long:")

# Replacing the occurrence of I am in the bio with I'm 
bio_replaced= bio.replace("I am " , " I'm " ) 

#Displaying all outputs using f-strings 
print(f"Your username is: {username.lower()}")
print(f"Your full name is: {full_name_title}")
print(f"Your bio message is: {bio_replaced}")