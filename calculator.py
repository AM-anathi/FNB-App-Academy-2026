# Multi-Funtion Calculator 
#using two number that perform all 4 basic arithmetic operations + two adavnced operations

num1 = float( input("Enter your first number: "))
num2 = float( input("Enter your second number: "))

# addition 
addition_result = num1 + num2 

# subtraction 
subtraction_result = num1 - num2 

# multiplication 
multiplication_result= num1 * num2


# Handling division by zero , 
# using if and else statement; this lets the program (1) make a decision, (2)check a condition 
# (3) runs different code depending on whether that condition is True or False
if num2 == 0: 
    print(f"Error: Cannot divide by zero! ")

else: 
    division_result = num1 / num2 
    floor_div_result = num1 // num2 
    modulus_result = num1 % num2
    print(f"Division result {round(division_result,2)}rounded")
    print(f"Floor division result {round(floor_div_result,2)} rounded")
    print(f"Modulus result {round(modulus_result,2)} rounded")

print(f"Addition result {round(addition_result,2)} rounded")
print(f"Subtraction result {round(subtraction_result,2)} rounded")
print(f"Multiplication result {round(multiplication_result,2)} rounded")
