'''  

The Rules:
Rock beats Scissors (rock blunts scissors). 
Scissors beats Paper (scissors cuts paper). 
Paper beats Rock (paper covers rock). 

'''

import random

print("Welcome to the Rock-Paper-Scissors Game")
Option = ['Rock','Paper','Scissors']
print(f"Kindly pick any one of the choice: {Option}")
User_Choice = input("Enter Your Choice: ")
Comp_Choice = random.choice(Option)

print(f"Your Choice : {User_Choice}, Computer Choice : {Comp_Choice}")

if User_Choice == Comp_Choice:
    print("Match Tie!! Both You & Computer picked up the same option.")

elif User_Choice == 'Rock':
    if Comp_Choice == 'Paper':
        print("Paper covers Rock, Computer win!")
    elif Comp_Choice == 'Scissors':
        print("Rock bluts Scissors, You win!")

elif User_Choice == 'Paper':
    if Comp_Choice == 'Rock':
        print("Paper covers Rock, You win!")
    if Comp_Choice == 'Scissors':
        print("Scissors cuts Paper, Computer win!")

elif User_Choice == 'Scissors':
    if Comp_Choice == 'Rock':
        print("Rock bluts Scissors, Computer win!")
    if Comp_Choice == 'Paper':
        print("Scissors cuts Paper, You win!")
