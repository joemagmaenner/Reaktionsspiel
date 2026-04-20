# 🎯 Reaktionszeit-Test

Ein simples GUI-Spiel mit **tkinter**: Warte auf den blauen Bildschirm — dann so schnell wie möglich klicken!

---

## Voraussetzungen

- Python 3.10 oder neuer
- Nur Standardbibliothek (`tkinter`, `random`, `time`) — kein `pip install` nötig

> ℹ️ Auf manchen Linux-Systemen muss tkinter nachinstalliert werden:
> ```bash
> sudo apt install python3-tk
> ```

---

## Starten

```bash
python main.py
```

Es öffnet sich ein 600×400 px großes Fenster.

---

## Spielablauf

| Schritt | Farbe | Aktion |
|---------|-------|--------|
| 1. Start | Grau `#444` | Klicken um zu starten |
| 2. Warten | Rot `#c0392b` | **Nicht klicken!** Warte auf Blau |
| 3. Signal | Blau `#1a6eb5` | **Sofort klicken!** |
| 4. Ergebnis | Dunkelblau `#1a1a2e` | Reaktionszeit + Bewertung wird angezeigt |
| 5. Wiederholen | — | Nochmal klicken für eine neue Runde |

> ⚠️ **Fehlstart:** Wer während der roten Phase klickt, bekommt eine Fehlermeldung und muss neu starten. Der Hintergrund wird dunkelrot (`#8B0000`).

---

## Bewertungsskala

| Reaktionszeit | Bewertung |
|---|---|
| unter 150 ms | Übernatürlich schnell! |
| 150 – 199 ms | Ausgezeichnet! |
| 200 – 249 ms | Sehr gut! |
| 250 – 299 ms | Gut |
| 300 – 399 ms | Durchschnitt |
| 400 ms+ | Übe weiter! |

---

## Technische Details

- **Framework:** tkinter (Canvas-basiert)
- **Fenstergröße:** 600×400 px, nicht skalierbar
- **Zufällige Wartezeit:** 1500–5000 ms (1,5–5 Sekunden)
- **Zeitmessung:** `time.perf_counter()` für hohe Präzision
- **Zustandsmaschine:** `waiting → red → blue → result → waiting`

---

## Projektstruktur

```
main.py      ← Hauptprogramm (einzige Datei)
README.md    ← diese Datei
```

---

## Klassen & Methoden

### `ReactionGame`

| Methode | Beschreibung |
|---|---|
| `__init__(root)` | Baut das Fenster und Canvas auf, setzt Startzustand |
| `set_color(color)` | Ändert die Hintergrundfarbe von Canvas und Fenster |
| `set_text(main, sub)` | Setzt Haupt- und Untertext auf dem Canvas |
| `on_click(event)` | Reagiert auf Klick je nach aktuellem Zustand |
| `start_red_phase()` | Startet die Wartephase (rot), plant `go_blue()` ein |
| `go_blue()` | Zeigt blaues Signal, startet Timer |
| `show_result(ms)` | Berechnet Bewertung und zeigt Ergebnis an |

---

## Tipps

- Die Wartezeit ist zufällig — nicht versuchen, den Rhythmus zu erraten
- Entspannt warten ist effektiver als angespannt starren
- Unter **250 ms** gilt als sehr gutes Ergebnis, unter **200 ms** als ausgezeichnet

---

## Lizenz

Frei verwendbar — kein Copyright, kein Stress.
