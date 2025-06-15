import random

def play_game(player_name):
    secret_number = random.randint(1, 100)
    attempts = 0

    print(f"\n👋 Hello {player_name}! Guess the number between 1 and 100.")

    while True:
        try:
            guess = int(input("👉 Your guess: "))
            attempts += 1

            if guess < secret_number:
                print("🔼 Too low!")
            elif guess > secret_number:
                print("🔽 Too high!")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                return attempts
        except ValueError:
            print("⚠️ Please enter a valid number.")
