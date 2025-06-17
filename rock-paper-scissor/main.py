import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input("Enter rock, paper, or scissors: ").lower()

if user_choice not in ['rock', 'paper', 'scissors']:
    print("Invalid choice. Please enter rock, paper, or scissors.")