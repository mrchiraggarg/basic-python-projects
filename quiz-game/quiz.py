import json
import random

def load_questions(filename="questions.json"):
    with open(filename, "r") as file:
        return json.load(file)

def ask_question(question_obj):
    question = question_obj["question"]
    options = question_obj["options"]
    answer = question_obj["answer"]

    print(f"\n{question}")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    try:
        choice = int(input("Enter your answer (1-4): "))
        if options[choice - 1] == answer:
            print("✅ Correct!")
            return True
        else:
            print(f"❌ Wrong! The correct answer is: {answer}")
            return False
    except (ValueError, IndexError):
        print("⚠️ Invalid input. Question skipped.")
        return False
