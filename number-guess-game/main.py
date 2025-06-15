from game import play_game
from scoreboard import save_score, show_top_scores

def main():
    print("🎮 Welcome to the Number Guessing Game!")

    while True:
        print("\nMenu:")
        print("1. Play Game")
        print("2. View Scoreboard")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            name = input("Enter your name: ")
            attempts = play_game(name)
            save_score(name, attempts)
        elif choice == "2":
            show_top_scores()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
