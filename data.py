import json
import os

FILE_NAME = "data.txt"

def add_score(name_game, name_user, time):
    """Speichert einen neuen Score als JSON-Objekt in einer neuen Zeile."""
    score_entry = {
        "name_game": name_game,
        "name_user": name_user,
        "time": time
    }
    
    try:
        with open(FILE_NAME, "a", encoding="utf-8") as f:
            # Wir schreiben das Dictionary als kompakten JSON-String + Zeilenumbruch
            f.write(json.dumps(score_entry) + "\n")
    except Exception as e:
        print(f"Fehler beim Speichern: {e}")

def load_scores():
    """Liest alle Scores aus der Datei und gibt sie als Liste von Dicts zurück."""
    scores = []
    
    if not os.path.exists(FILE_NAME):
        return scores

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:  # Überspringe Leerzeilen
                    scores.append(json.loads(line))
    except Exception as e:
        print(f"Fehler beim Laden: {e}")
        
    return scores