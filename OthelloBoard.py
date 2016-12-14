from Game import *
from tkinter import *

WIDTH = 500
HEIGHT = 500
PADDING = 50
TILEPADDING = 5

class OthelloBoard(Frame):

    def __init__(self, root, N, board, playerX, playerXTurn):
        Frame.__init__(self, root)

        self.canvas = Canvas(self, width = WIDTH, height = HEIGHT, bg="#AF7541")
        self.root = root
        self.board = board
        self.playerX = playerX
        self.playerXTurn = playerXTurn

        self.root.title("Othello")
        self.pack(fill=BOTH, expand=1)

        self.updateBoard(N, self.board, (0, 0), playerXTurn)

    def updateBoard(self, N, board, score, playerXTurn):
        self.canvas.delete("all")
        self.board = board

        turnText = "Player X's turn!" if playerXTurn else "Player Y's turn!"
        self.canvas.create_text(WIDTH/2, PADDING/2, anchor="center", text=turnText)

        playerX, playerY = ("Black", "White") if self.playerX == "B" else ("White", "Black")
        scoreText = "Player X (%s) Score: %s    VS    Player Y (%s) Score: %s" % (playerX, score[0], playerY, score[1])
        self.canvas.create_text(WIDTH/2, HEIGHT - PADDING/2, anchor="center", text=scoreText)

        tileLength = (WIDTH - 2*PADDING) / N
        pieceLength = tileLength - 2*TILEPADDING

        for i,row in enumerate(self.board):
            for j,col in enumerate(row):
                self.canvas.grid(row=i,column=j)
                tileColor = "#007E0B" if ((i + j) % 2 == 0) else "#009D0D"

                tileMinX, tileMinY = PADDING + i*tileLength, PADDING + j*tileLength
                tileMaxX, tileMaxY = tileMinX + tileLength, tileMinY + tileLength

                self.canvas.create_rectangle(tileMinX, tileMinY, tileMaxX, tileMaxY, outline="black", fill=tileColor)

                pieceMinX, pieceMinY = tileMinX + TILEPADDING, tileMinY + TILEPADDING
                pieceMaxX, pieceMaxY = pieceMinX + pieceLength, pieceMinY + pieceLength

                if self.board[i][j] != ' ':
                    pieceColor = 'white' if self.board[i][j] == 'W' else 'black'

                    self.canvas.create_oval(pieceMinX, pieceMinY, pieceMaxX, pieceMaxY, fill=pieceColor, tags="oval")