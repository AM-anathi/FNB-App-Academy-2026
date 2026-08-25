# The Secure Password Hint Tool 

user = input("Enter your secret password: ").strip()
print(f"Your password hint: it starts with {user[0].upper} and ends with {user[-1].upper}") 