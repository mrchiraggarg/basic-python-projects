import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
# user_choice = input("Enter rock, paper, or scissors: ").lower()

print("Welcome to Rock, Paper, Scissors!")
print("You can choose from:")
print("Type 1 For Rock")
print("Type 2 For Paper")
print("Type 3 For Scissors")

user_choice = int(input("Enter your choice: "))

try:
    if user_choice < 1 or user_choice > 3:
        print("Invalid choice. Please enter rock, paper, or scissors.")

except Exception as e:
    print(f"❌ Error: {e}")