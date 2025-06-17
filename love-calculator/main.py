import random

def love_calculator(name1, name2):
    # Normalize names
    name1 = name1.strip().lower()
    name2 = name2.strip().lower()

    # Combine names and generate seed
    combined = name1 + name2
    random.seed(sum(ord(char) for char in combined))  # consistent for same names
    score = random.randint(0, 100)

    # Generate message based on score
    if score >= 80:
        message = "❤️ Perfect match! You're made for each other!"
    elif score >= 60:
        message = "😊 Good match! There's potential!"
    elif score >= 40:
        message = "🙂 Not bad! Worth a shot!"
    elif score >= 20:
        message = "😐 Could work... maybe."
    else:
        message = "💔 Uhh... maybe stay friends?"

    return score, message

# Take input
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

score, result_message = love_calculator(name1, name2)
print(f"Love Score: {score}%")
print(result_message)
