import tkinter as tk
from tkinter import messagebox
import json
import random

# Load flashcards from JSON file
def load_flashcards():
    try:
        with open("flashcards.json", "r") as f:
            return json.load(f)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load flashcards: {e}")
        return []

# Flashcard App class
class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Flashcard App")
        self.root.geometry("500x300")
        self.root.configure(bg="#1e1e1e")

        self.cards = load_flashcards()
        self.current = {}
        self.showing_answer = False
        self.score = {"correct": 0, "incorrect": 0}

        self.card_text = tk.Label(root, text="", font=("Arial", 16), wraplength=400, bg="#1e1e1e", fg="#FFD700")
        self.card_text.pack(pady=40)

        button_frame = tk.Frame(root, bg="#1e1e1e")
        button_frame.pack()

        self.flip_btn = tk.Button(button_frame, text="🔁 Flip", width=10, command=self.flip_card)
        self.flip_btn.grid(row=0, column=0, padx=5)

        self.correct_btn = tk.Button(button_frame, text="✅ Correct", width=10, command=self.mark_correct)
        self.correct_btn.grid(row=0, column=1, padx=5)

        self.wrong_btn = tk.Button(button_frame, text="❌ Incorrect", width=10, command=self.mark_incorrect)
        self.wrong_btn.grid(row=0, column=2, padx=5)

        self.status_label = tk.Label(root, text="", font=("Arial", 12), bg="#1e1e1e", fg="#00FF99")
        self.status_label.pack(pady=10)

        self.next_card()

    def next_card(self):
        if not self.cards:
            self.card_text.config(text="🎉 You've gone through all flashcards!")
            self.flip_btn.config(state=tk.DISABLED)
            self.correct_btn.config(state=tk.DISABLED)
            self.wrong_btn.config(state=tk.DISABLED)
            return

        self.current = random.choice(self.cards)
        self.card_text.config(text=f"❓ {self.current['question']}")
        self.showing_answer = False

    def flip_card(self):
        if self.showing_answer:
            self.card_text.config(text=f"❓ {self.current['question']}")
        else:
            self.card_text.config(text=f"💡 {self.current['answer']}")
        self.showing_answer = not self.showing_answer

    def mark_correct(self):
        self.score["correct"] += 1
        self.cards.remove(self.current)
        self.update_status()
        self.next_card()

    def mark_incorrect(self):
        self.score["incorrect"] += 1
        self.update_status()
        self.next_card()

    def update_status(self):
        correct = self.score["correct"]
        incorrect = self.score["incorrect"]
        self.status_label.config(text=f"✅ Correct: {correct} | ❌ Incorrect: {incorrect}")

# Launch the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
