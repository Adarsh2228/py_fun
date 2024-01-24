import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")

# Create the game board
board = [[" " for _ in range(3)] for _ in range(3)]

# Create the buttons for each cell
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text=" ", font=("Arial", 20), width=6, height=3,
                           command=lambda r=row, c=col: make_move(r, c))
        button.grid(row=row, column=col, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)

# Create a label to display the current player
current_player_label = tk.Label(window, text="Player X's turn", font=("Arial", 16))
current_player_label.grid(row=3, columnspan=3, pady=10)

# Create a function to handle button clicks
def make_move(row, col):
    global board
    if board[row][col] == " ":
        board[row][col] = "X" if current_player_label.cget("text") == "Player X's turn" else "O"
        buttons[row][col].config(text=board[row][col])
        check_winner()
        current_player_label.config(text="Player O's turn" if current_player_label.cget("text") == "Player X's turn" else "Player X's turn")
    else:
        messagebox.showerror("Invalid Move", "This cell is already occupied!")

# Create a function to check for a winner
def check_winner():
    global board
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            messagebox.showinfo("Game Over", f"Player {board[i][0]} wins!")
            reset_game()
            return
        if board[0][i] == board[1][i] == board[2][i] != " ":
            messagebox.showinfo("Game Over", f"Player {board[0][i]} wins!")
            reset_game()
            return
    if board[0][0] == board[1][1] == board[2][2] != " ":
        messagebox.showinfo("Game Over", f"Player {board[0][0]} wins!")
        reset_game()
        return
    if board[0][2] == board[1][1] == board[2][0] != " ":
        messagebox.showinfo("Game Over", f"Player {board[0][2]} wins!")
        reset_game()
        return
    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        messagebox.showinfo("Game Over", "It's a tie!")
        reset_game()

# Create a function to reset the game
def reset_game():
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]
    for row in buttons:
        for button in row:
            button.config(text=" ")
    current_player_label.config(text="Player X's turn")

# Start the main loop
window.mainloop()
