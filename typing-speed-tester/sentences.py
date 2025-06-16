import random

sentences = [
    "Python is a great programming language.",
    "Typing speed depends on accuracy and practice.",
    "The quick brown fox jumps over the lazy dog.",
    "Practice makes a man perfect.",
    "Artificial intelligence is the future."
]

def get_random_sentence():
    return random.choice(sentences)
