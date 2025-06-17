import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try: 
    length = int(input("Enter a length of password: "))
    print(generate_password(length))
except ValueError:
    print("Please enter a valid integer for the password length.")