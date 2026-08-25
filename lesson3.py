# adding two numbers 

#num1 = input("Enter the first number") # input taks the value as text instead of numbers 
#num2 = input("Enter the second number")
#want to output the sum onto the terminal 

#string contatination ("Hello" + "World" = "HelloWorld") same as ("5" +"10" = "510")
#print(num1+num2) #output 510

#Core Data Type 
#str: String/Text "hello" "j8%&"
#int: integar/whole number 5, -1, 10
# float : decimal numbers 5.24, 6.1
#bool : True or False 

#Type Casting (converting form one date type to another)
#print(int(num1) + (int (num2)) )

#Calculating the tip 

bill = float(input("Enter the bill: R"))   #when work with money we use decimal points 
tip = 0.15 #Written in decimal 

val_tip = bill * tip 
total_cost = bill + val_tip

print(f"Here is the trip : {val_tip}")
print(f"Here is the trip : {round (val_tip, 2)} rounded")

print(f"Here is the total cost : {total_cost}")
print(f"Here is the total cost : {round (total_cost, 2)} rounded")

