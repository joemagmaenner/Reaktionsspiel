import os
import data

def run_test():
    # 1. Vorbereitung: Test-Dateiname definieren und alte Test-Daten löschen
    test_file = "data.txt"
    if os.path.exists(test_file):
        os.remove(test_file)
    
    print("--- Starte Test für data.py ---")

    # 2. Testdaten definieren
    sample_scores = [
        {"name_game": "Tetris", "name_user": "Alex", "time": "120"},
        {"name_game": "Pacman", "name_user": "Sam", "time": "300"},
        {"name_game": "Snake", "name_user": "Chris", "time": "45"}
    ]

    # 3. add_score() testen
    print("Teste add_score()...")
    for score in sample_scores:
        data.add_score(score["name_game"], score["name_user"], score["time"])
    
    # 4. load_scores() testen
    print("Teste load_scores()...")
    loaded_scores = data.load_scores()

    # 5. Validierung
    if len(loaded_scores) == len(sample_scores):
        print(f"Erfolg: {len(loaded_scores)} Einträge wurden korrekt geladen.")
    else:
        print(f"FEHLER: Erwartete {len(sample_scores)} Einträge, aber habe {len(loaded_scores)} erhalten.")
        return

    # Detail-Check
    for i in range(len(sample_scores)):
        original = sample_scores[i]
        loaded = loaded_scores[i]
        
        if (original["name_game"] == loaded["name_game"] and 
            original["name_user"] == loaded["name_user"] and 
            str(original["time"]) == str(loaded["time"])):
            print(f"  [OK] Eintrag {i+1}: {loaded['name_user']} - {loaded['name_game']}")
        else:
            print(f"  [FEHLER] Abweichung in Eintrag {i+1}!")
            print(f"  Erwartet: {original}")
            print(f"  Erhalten: {loaded}")

    print("--- Test abgeschlossen ---")

if __name__ == "__main__":
    run_test()