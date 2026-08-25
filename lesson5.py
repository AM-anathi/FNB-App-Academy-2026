#while and for loops 
#loops repeat code multiple times 
# A countdown using while loop
#count = 4 

#while count > 0 :  # conditional operator working with two value 
    #print(count)
    #count = count - 1

#print("Blast Off !!!")

#Building a simple rep counter 
#for rep in range(1,4):  #range tells python to start from 1 and end at 3
   # print (f"This is rep no.{rep}")

# A Guessing game 
secret_word ="python"

while True: 
    guess = input("Guess the programming language we are using:").lower()

    if guess == secret_word : 
        print("You guessed the correct language !!!")
        break #used to exist a loop
    else: 
     print("Incorrect guess try again")


