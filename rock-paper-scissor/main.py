import random

try:
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    # user_choice = input("Enter rock, paper, or scissors: ").lower()

    print("Welcome to Rock, Paper, Scissors!")
    print("Please type to select:")
    print("1 For Rock")
    print("2 For Paper")
    print("3 For Scissors")

    user_choice = int(input("Enter your choice: "))


    if user_choice < 1 or user_choice > 3:
        print("Invalid choice. Please enter 1, 2, or 3.")

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

except Exception as e:
    print(f"❌ Error: {e}")