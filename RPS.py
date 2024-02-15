import random

user_win = 0
computer_win = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock, Paper, Scissors or Q to quit: ")
    if user_input.lower() == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #rock = 0, paper = 1 and scissors = 2

    computer_choice = options[random_number]
    if user_input == "rock" and computer_choice == "scissors":
        print("You chose ", user_input, "and the computer chose", computer_choice)
        print("You won!")
        user_win += 1
    elif user_input == "paper" and computer_choice == "rock":
        print("You chose ", user_input, "and the computer chose", computer_choice)
        user_win += 1
        print("You won!")
    elif user_input == "scissors" and computer_choice == "paper":
        print("You chose ", user_input, "and the computer chose", computer_choice)
        user_win += 1
        print("You won!")
    elif user_input == computer_choice:
        print("No contest!")
    else:
        print("You chose ", user_input, "and the computer chose", computer_choice)
        computer_win += 1
        print("You lose")
    continue
    
print(f"Your score is {user_win}.")
print(f"The computer score is {computer_win}.")
print("Goodbye!")