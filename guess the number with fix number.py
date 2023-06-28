number=8
user_input=int(input("Guess the number 1-10:"))
if user_input > 8:
    print("You have choosed higher number")
elif user_input <=7:
    print("you have guessed  low number")
elif user_input == 8:
    print("you have guessed correct number")
else:
    print("Plese guess the valid number")

