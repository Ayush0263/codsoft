#WAP to make a rock paper scissor game.
import random


def get_user_choice():
    while True:
        user_choice = input("Please choose from the  Rock, Paper, or Scissors:- ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print('''                                               DANGER 
                     Invalid choice. Please choose only between Rock, Paper, or Scissors:-''')


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"


def main():
    print("Welcome to my game the Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}.")
        print(f" The Computer choice is-- {computer_choice}.")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print("Thanks for playing! It's my first code")


if __name__ == "__main__":
    main()
