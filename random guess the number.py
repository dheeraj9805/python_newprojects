import random

number=random.randrange(1,10)
User_input= int(input("Enter the number between 1-10 : "))
while number != User_input:
    if User_input < number:
        print("Too Low")
        User_input= int(input("Enter the number between 1-10 : "))
    elif User_input > number:
        print("Too high")
        User_input= int(input("Enter the number between 1-10 : "))
    else:
        break
print("you guessed it right")
    
    
