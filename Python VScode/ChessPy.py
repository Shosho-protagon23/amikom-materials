import tkinter as tk
from tkinter import messagebox
import chess
import chess.svg

class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Catur Sederhana")
        self.board = chess.Board()
        self.selected_square = None
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()
        self.status_label = tk.Label(root, text="Giliran: Putih")
        self.status_label.pack()

    def draw_board(self):
        self.canvas.delete("all")
        square_size = 50
        colors = ["#f0d9b5", "#b58863"]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                x1, y1 = col * square_size, row * square_size
                x2, y2 = x1 + square_size, y1 + square_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                piece = self.board.piece_at(chess.square(col, 7 - row))
                if piece:
                    piece_symbol = self.get_piece_symbol(piece)
                    self.canvas.create_text(x1 + 25, y1 + 25, text=piece_symbol, font=("Arial", 24))

    def get_piece_symbol(self, piece):
        symbols = {
            chess.Piece(chess.PAWN, chess.WHITE): "♙",
            chess.Piece(chess.KNIGHT, chess.WHITE): "♘",
            chess.Piece(chess.BISHOP, chess.WHITE): "♗",
            chess.Piece(chess.ROOK, chess.WHITE): "♖",
            chess.Piece(chess.QUEEN, chess.WHITE): "♕",
            chess.Piece(chess.KING, chess.WHITE): "♔",
            chess.Piece(chess.PAWN, chess.BLACK): "♟",
            chess.Piece(chess.KNIGHT, chess.BLACK): "♞",
            chess.Piece(chess.BISHOP, chess.BLACK): "♝",
            chess.Piece(chess.ROOK, chess.BLACK): "♜",
            chess.Piece(chess.QUEEN, chess.BLACK): "♛",
            chess.Piece(chess.KING, chess.BLACK): "♚",
        }
        return symbols.get(piece, "?")

    def on_click(self, event):
        col = event.x // 50
        row = 7 - (event.y // 50)
        square = chess.square(col, row)
        
        if self.selected_square is None:
            if self.board.piece_at(square) and self.board.color_at(square) == self.board.turn:
                self.selected_square = square
                self.highlight_square(square)
        else:
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.selected_square = None
                self.draw_board()
                self.update_status()
                if self.board.is_checkmate():
                    winner = "Hitam" if self.board.turn == chess.WHITE else "Putih"
                    messagebox.showinfo("Game Over", f"Checkmate! {winner} menang.")
                    self.root.quit()
                elif self.board.is_stalemate():
                    messagebox.showinfo("Game Over", "Stalemate! Seri.")
                    self.root.quit()
            else:
                self.selected_square = None
                self.draw_board()

    def highlight_square(self, square):
        col = chess.square_file(square)
        row = 7 - chess.square_rank(square)
        x1, y1 = col * 50, row * 50
        x2, y2 = x1 + 50, y1 + 50
        self.canvas.create_rectangle(x1, y1, x2, y2, outline="red", width=3)

    def update_status(self):
        turn = "Putih" if self.board.turn == chess.WHITE else "Hitam"
        self.status_label.config(text=f"Giliran: {turn}")

if __name__ == "__main__":
    root = tk.Tk()
    game = ChessGame(root)
    root.mainloop()
