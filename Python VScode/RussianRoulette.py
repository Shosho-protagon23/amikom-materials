import tkinter as tk
from tkinter import messagebox
import random

class RussianRoulette:
    def __init__(self, root):
        self.root = root
        self.root.title("Russian Roulette: Player vs Bot")
        self.chambers = [False] * 6  # 6 chambers, False = empty, True = bullet
        self.bullet_position = random.randint(0, 5)
        self.chambers[self.bullet_position] = True
        self.current_player = "Player"  # Start with player
        self.shots_taken = 0
        
        # GUI Elements
        self.label = tk.Label(root, text="Russian Roulette\nKlik 'Tarik Pelatuk' untuk mulai.\nPeluru di salah satu dari 6 chamber.")
        self.label.pack(pady=10)
        
        self.button = tk.Button(root, text="Tarik Pelatuk", command=self.pull_trigger)
        self.button.pack(pady=10)
        
        self.status_label = tk.Label(root, text=f"Giliran: {self.current_player}")
        self.status_label.pack(pady=10)

    def pull_trigger(self):
        if self.shots_taken >= 6:
            messagebox.showinfo("Game Over", "Semua chamber sudah ditembak. Game reset.")
            self.reset_game()
            return
        
        chamber = self.shots_taken
        self.shots_taken += 1
        
        if self.chambers[chamber]:
            loser = self.current_player
            messagebox.showinfo("Game Over", f"BANG! {loser} kalah! Peluru ada di chamber {chamber + 1}.")
            self.reset_game()
        else:
            messagebox.showinfo("Selamat", f"CLICK! {self.current_player} selamat. Chamber {chamber + 1} kosong.")
            self.switch_turn()
            if self.current_player == "Bot":
                self.root.after(1000, self.bot_turn)  # Bot plays after 1 second

    def bot_turn(self):
        self.pull_trigger()

    def switch_turn(self):
        self.current_player = "Bot" if self.current_player == "Player" else "Player"
        self.status_label.config(text=f"Giliran: {self.current_player}")

    def reset_game(self):
        self.chambers = [False] * 6
        self.bullet_position = random.randint(0, 5)
        self.chambers[self.bullet_position] = True
        self.current_player = "Player"
        self.shots_taken = 0
        self.status_label.config(text=f"Giliran: {self.current_player}")
        self.label.config(text="Russian Roulette\nKlik 'Tarik Pelatuk' untuk mulai.\nPeluru di salah satu dari 6 chamber.")

if __name__ == "__main__":
    root = tk.Tk()
    game = RussianRoulette(root)
    root.mainloop()
