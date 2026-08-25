# contact book that stores contacts as a list of dictionaries and allows users to add, search, view and delete contacts

def add_contact( contacts, name, phone, email):
   contact = {
      "name" : name , 
      "phone": phone, 
      "email": email 
   }
   contacts.append(contact)
   print(f"Contact has been added") 

# search contact by name function    
def search_contact(contacts,name):
   for contact in contacts: 
      if contact["name"] == name :
         return contact
   return None
   
# delete contact function that remove a contact by name 
def delete_contact(contacts, name):
   contact = search_contact(contacts, name)
   if contact: 
      contacts.remove(contact) 
      print(f"{name} has been deleted!")
   else : 
      print("Contact not found. ")

# displaying all contacts in a formatted layout 
def view_all(contacts): 
   if len(contacts) == 0 :
     print("No contacts found.")
   else: 
    for contact in contacts:
       print(f"Name: {contact['name']}")
       print(f"Phone:{contact['phone']}")
       print(f"Email:{contact['email']}")
       print("-------------------------")

# Menu 
contacts =[] 
while True :
   print("\nChoose an action")
   print("1 = Add Contact")
   print("2 = Search Contact")
   print("3 = Delet Contact ")
   print("4 = View All Contacts")
   print("5 = Exit")

   action = input("Enter your choice:") # stores on choice the user makes 
   if action == "1":
       name = input("Name: ")
       phone = input("Phone: ")
       email = input("Email: ")
       add_contact(contacts,name, phone, email)

   elif action == "2": 
      name = input("Search name: ")
      result = search_contact(contacts, name)
      print(result if result else "Not found")

   elif action == "3": 
      name = input("Delete name: ")
      delete_contact(contacts, name)
 
   elif action == "4":
      view_all(contacts)
   elif action == "5": 
      print("Goodbye!")
      break 
   else: 
      print("Invalid choice, try again!")


