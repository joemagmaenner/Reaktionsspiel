"""
Reaktionszeitmesser mit Highscore
Drücke ENTER wenn das Signal erscheint — so schnell wie möglich!
"""

import time
import random
import json
import os


HIGHSCORE_FILE = "highscores.json"
MAX_SCORES = 10


def clear_screen() -> None:
    """Löscht den Bildschirm."""
    pass


def get_player_name() -> str:
    """Fragt nach dem Spielernamen."""
    pass


def wait_and_measure() -> float:
    """
    Wartet 2-5 Sek., zeigt dann 'JETZT!' und misst wie lange
    der Spieler braucht um ENTER zu drücken.

    Returns:
        Reaktionszeit in ms, oder -1 bei Fehlstart.
    """
    pass


def load_highscores() -> list[dict]:
    """
    Lädt Highscores aus JSON-Datei.

    Returns:
        Liste von {"name": str, "ms": float}
    """
    pass


def save_highscores(scores: list[dict]) -> None:
    """Speichert Highscores in JSON-Datei."""
    pass


def add_to_highscores(name: str, ms: float) -> int:
    """
    Fügt Ergebnis ein (aufsteigend sortiert, max. 10 Einträge).

    Returns:
        Platzierung (1-basiert), oder -1 wenn kein Highscore.
    """
    pass


def show_highscores() -> None:
    """Gibt die Highscore-Tabelle formatiert aus."""
    pass


def main() -> None:
    """
    Haupt-Loop:
      1. Spieler-Namen eingeben
      2. Reaktion messen
      3. Ergebnis & Highscore anzeigen
      4. Nochmal spielen? (j/n)
    """
    pass


if __name__ == "__main__":
    main()
