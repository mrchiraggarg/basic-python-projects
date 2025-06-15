from quiz import load_questions, ask_question

def start_quiz():
    print("🎉 Welcome to the Python Quiz Game!")
    questions = load_questions()
    random.shuffle(questions)

    score = 0
    for q in questions:
        if ask_question(q):
            score += 1

    print(f"\n🏁 Quiz finished! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    start_quiz()
