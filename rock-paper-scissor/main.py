import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
# user_choice = input("Enter rock, paper, or scissors: ").lower()

print("Welcome to Rock, Paper, Scissors!")
print("You can choose from:")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

user_choice = int(input("Enter your choice (1, 2, or 3): "))

if user_choice not in ['rock', 'paper', 'scissors']:
    print("Invalid choice. Please enter rock, paper, or scissors.")