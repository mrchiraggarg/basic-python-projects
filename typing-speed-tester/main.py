import tkinter as tk
from tkinter import messagebox
import time
from sentences import get_random_sentence

start_time = 0

def start_test():
    global start_time, sentence
    sentence = get_random_sentence()
    sentence_label.config(text=sentence)
    input_text.delete(0, tk.END)
    result_label.config(text="")
    start_time = time.time()

def calculate_result():
    end_time = time.time()
    typed = input_text.get()
    time_taken = end_time - start_time

    if not typed.strip():
        messagebox.showerror("Error", "You must type something!")
        return

    words = len(typed.split())
    wpm = round(words / (time_taken / 60), 2)

    correct_chars = 0
    for i, c in enumerate(typed):
        if i < len(sentence) and c == sentence[i]:
            correct_chars += 1
    accuracy = round((correct_chars / len(sentence)) * 100, 2)

    result_label.config(
        text=f"⌛ Time: {round(time_taken, 2)}s  |  🧠 Accuracy: {accuracy}%  |  🚀 WPM: {wpm}",
        fg="#00BFFF"
    )

# GUI Setup
root = tk.Tk()
root.title("⌨️ Typing Speed Tester")
root.geometry("600x300")
root.configure(bg="#1E1E1E")
root.resizable(False, False)

# Widgets
title_label = tk.Label(root, text="Typing Speed Tester", font=("Arial", 20, "bold"), bg="#1E1E1E", fg="#FFD700")
title_label.pack(pady=10)

sentence_label = tk.Label(root, text="", wraplength=550, font=("Arial", 14), bg="#1E1E1E", fg="white")
sentence_label.pack(pady=10)

input_text = tk.Entry(root, font=("Arial", 14), width=60)
input_text.pack(pady=10)

button_frame = tk.Frame(root, bg="#1E1E1E")
button_frame.pack(pady=10)

start_btn = tk.Button(button_frame, text="Start", font=("Arial", 12), command=start_test)
start_btn.pack(side=tk.LEFT, padx=10)

done_btn = tk.Button(button_frame, text="Done", font=("Arial", 12), command=calculate_result)
done_btn.pack(side=tk.LEFT, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 13), bg="#1E1E1E", fg="white")
result_label.pack(pady=10)

root.mainloop()
