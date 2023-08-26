print("Welcome to RPS Game Zone")

import random

def get_player_choice():
    player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while player_choice not in ["rock", "paper", "scissors"]:
        player_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return player_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

