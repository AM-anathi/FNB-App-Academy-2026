# The Smart ATM withdrawal simulator 
# A bank transaction checking if a user has enoungh money 

balance = 500 # bank balance
withdraw = float(input("How much money would you want to withdraw ? R:"))
if withdraw <= 0 : # if the user wants to withdraw a negative amount or zero
    print(f"Invalid amount.\n You must withdraw more the R0")

elif withdraw <= balance :
    print( f"Withdrawal successful! \nYour Remaining balance R:{balance - withdraw}")

else:
    print(f"Declined!\nInsufficient funds.")

word = "Computer" 
print(word[-3])