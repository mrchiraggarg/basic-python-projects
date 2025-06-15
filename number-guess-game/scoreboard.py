import json
import os

FILENAME = "scores.json"

def load_scores():
    if not os.path.exists(FILENAME):
        return []

    try:
        with open(FILENAME, "r") as f:
            data = f.read().strip()
            if not data:  # File is empty
                return []
            return json.loads(data)
    except (json.JSONDecodeError, ValueError):
        print("⚠️ Warning: scores.json is corrupted or invalid. Resetting scores.")
        return []

def save_score(player_name, attempts):
    scores = load_scores()
    scores.append({"name": player_name, "attempts": attempts})
    scores.sort(key=lambda x: x["attempts"])  # sort by attempts (lowest first)

    with open(FILENAME, "w") as f:
        json.dump(scores, f, indent=2)

def show_top_scores(limit=5):
    scores = load_scores()
    print("\n🏆 Top Scores:")
    for i, entry in enumerate(scores[:limit], start=1):
        print(f"{i}. {entry['name']} - {entry['attempts']} attempts")
