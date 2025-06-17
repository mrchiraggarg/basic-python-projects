import random

def play_game():
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print("Welcome to Rock, Paper, Scissors!")
    print("Please type to select:")
    print("1 For Rock")
    print("2 For Paper")
    print("3 For Scissors")

    try:
        user_choice = int(input("Enter your choice: "))

        if user_choice < 1 or user_choice > 3:
            print("Invalid choice. Please enter 1, 2, or 3.")
            return False
        else:
            if user_choice == 1:
                user_choice = 'rock'
            elif user_choice == 2:
                user_choice = 'paper'
            elif user_choice == 3:
                user_choice = 'scissors'

            print(f"You chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")

            if user_choice == computer_choice:
                print("It's a tie!")
            elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                 (user_choice == 'paper' and computer_choice == 'rock') or \
                 (user_choice == 'scissors' and computer_choice == 'paper'):
                print("You win! 🎉")
            else:
                print("You lose! 😢")
            return True
    except ValueError:
        print("Please enter a valid number (1, 2, or 3)")
        return False

def main():
    while True:
        game_completed = play_game()
        if game_completed:
            print("Wanna play again? (y/n)")
            play_again = input().strip().lower()
            if play_again != 'y':
                print("Thanks for playing! 🎮")
                break
        else:
            print("Let's try again!")

if __name__ == "__main__":
    main()