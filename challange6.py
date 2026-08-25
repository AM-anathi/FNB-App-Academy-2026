# The phone Directory Search 
contacts ={
    "Thembi":"0823461237",
    "Anna": "062567365", 
    "Lerato":"0765439865"

}
name=input(f"Enter the name of the contact whom you are looking for:  ")
if name in contacts :
 print(f"Found! {name}'s number is {contacts[name]}") 
else:
 print(f"Contact not found")
 