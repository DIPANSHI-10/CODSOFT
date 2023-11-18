import random

# creating function that prompts the user to choose rock,paper, scissors and return their choice
def get_user_choice():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice.Please choose rock, paper, or scissors. ")
        user_choice = input("Choose rock, paper, or scissors : ").lower()
    return user_choice
    
# Creating a function to get User's Choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Creating the function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
     ):
        return "You win!"
    else:
        return  "Computer wins!"
    
## Creating a function to diplay the result
def display_result(user_choice, computer_choice ,result):
    print(f" You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")
    print(result)

user_score = 0
computer_score= 0

# Creating a Main Game loop
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, result)

    ## Keeping Track of the scores
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    # Display scores 
    print(f"Your Score: {user_score}, Computer score: {computer_score}")

    play_again = input("Do you want to play again?  (yes/no): ").lower()
    if play_again != 'yes':
        break
