# The South African Fuel Cost Calculator 
#calculating travel costs 

kilometers = float(input("How many kilometers do you want to drive ? "))
petrol_price = float(input("What is your current petrol price per liter ?"))
# how must liters of fuels the car uses per kilometers 

liters_needed = kilometers/10 

#total cost 
total_cost = liters_needed * petrol_price 
print(f"Your final cost is {round(total_cost,2)}")
