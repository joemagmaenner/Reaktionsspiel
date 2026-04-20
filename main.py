import tkinter as tk
import random
import time
import os

HIGHSCORE_FILE = "reaction_highscores.txt"
MAX_HIGHSCORES = 5  # nur die besten 5 speichern

class ReactionGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Reaktionszeit-Test")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.state = "waiting"
        self.start_time = None
        self.after_id = None

        self.highscores = self.load_highscores()

        self.canvas = tk.Canvas(root, width=600, height=400, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.label = self.canvas.create_text(
            300, 150,
            text="Klicke, um zu starten",
            font=("Helvetica", 28, "bold"),
            fill="white"
        )
        self.sublabel = self.canvas.create_text(
            300, 200,
            text="",
            font=("Helvetica", 16),
            fill="white"
        )
        self.highscore_text = self.canvas.create_text(
            300, 300,
            text=self.format_highscores(),
            font=("Helvetica", 14),
            fill="yellow"
        )

        self.canvas.bind("<Button-1>", self.on_click)
        self.set_color("#444444")

    def set_color(self, color):
        self.canvas.configure(bg=color)
        self.root.configure(bg=color)

    def set_text(self, main, sub=""):
        self.canvas.itemconfig(self.label, text=main)
        self.canvas.itemconfig(self.sublabel, text=sub)

    def load_highscores(self):
        if not os.path.exists(HIGHSCORE_FILE):
            return []
        with open(HIGHSCORE_FILE, "r") as f:
            scores = [float(line.strip()) for line in f.readlines()]
            return sorted(scores)

    def save_highscores(self):
        with open(HIGHSCORE_FILE, "w") as f:
            for score in self.highscores[:MAX_HIGHSCORES]:
                f.write(f"{score}\n")

    def format_highscores(self):
        if not self.highscores:
            return "Keine Highscores yet"
        text = "Highscores:\n"
        for i, score in enumerate(self.highscores[:MAX_HIGHSCORES], 1):
            text += f"{i}. {score:.1f} ms\n"
        return text.strip()

    def update_highscore_display(self):
        self.canvas.itemconfig(self.highscore_text, text=self.format_highscores())

    def on_click(self, event):
        if self.state == "waiting":
            self.start_red_phase()

        elif self.state == "red":
            if self.after_id:
                self.root.after_cancel(self.after_id)
                self.after_id = None
            self.state = "waiting"
            self.set_color("#8B0000")
            self.set_text("Zu früh! Klicke zum Wiederholen")

        elif self.state == "blue":
            reaction_time = (time.perf_counter() - self.start_time) * 1000
            self.state = "result"
            self.set_color("#1a1a2e")
            self.show_result(reaction_time)

        elif self.state == "result":
            self.state = "waiting"
            self.set_color("#444444")
            self.set_text("Klicke, um erneut zu starten")

    def start_red_phase(self):
        self.state = "red"
        self.set_color("#c0392b")
        self.set_text("Warte...", "Nicht klicken - warte auf Blau!")
        delay = random.randint(1500, 5000)
        self.after_id = self.root.after(delay, self.go_blue)

    def go_blue(self):
        self.after_id = None
        self.state = "blue"
        self.start_time = time.perf_counter()
        self.set_color("#1a6eb5")
        self.set_text("JETZT! Klicke!", "")

    def show_result(self, ms):
        if ms < 150:
            rating = "Übernatürlich schnell!"
        elif ms < 200:
            rating = "Ausgezeichnet!"
        elif ms < 250:
            rating = "Sehr gut!"
        elif ms < 300:
            rating = "Gut"
        elif ms < 400:
            rating = "Durchschnitt"
        else:
            rating = "Übe weiter!"

        self.set_text(f"{ms:.1f} ms  -  {rating}", "Klicke zum Wiederholen")

        # Highscore aktualisieren
        self.highscores.append(ms)
        self.highscores.sort()
        self.save_highscores()
        self.update_highscore_display()


if __name__ == "__main__":
    root = tk.Tk()
    game = ReactionGame(root)
    root.mainloop()
