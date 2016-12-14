from Game import *
from tkinter import *
from unittest import mock

WIDTH = 500
HEIGHT = 525
PADDING = 50
TILEPADDING = 5

class OthelloBoard(Frame):

    def __init__(self, root, N, board, playerX, playerY, playerXTurn):
        Frame.__init__(self, root)

        self.canvas = Canvas(self, width = WIDTH, height = HEIGHT, bg="#AF7541")
        self.root = root
        self.board = board
        self.playerX = playerX
        self.playerY = playerY
        self.playerXTurn = playerXTurn
        self.tileLength = (WIDTH - 2*PADDING) / N
        self.pieceLength = self.tileLength - 2*TILEPADDING

        self.root.title("Othello")
        self.pack(fill=BOTH, expand=1)

        self.updateBoard(N, self.board, (0, 0), playerXTurn)

    def updateBoard(self, N, board, score, playerXTurn):
        self.canvas.delete("all")
        self.board = board

        turnText = ""

        if playerXTurn is None:
            turnText = "It's a tie!" if score[0] == score[1] else ("Player X won!" if score[0] > score[1] else "Player Y won!")
        else:
            turnText = "Player X's turn!" if playerXTurn else "Player Y's turn!"

        self.canvas.create_text(WIDTH/2, PADDING/2, anchor="center", text=turnText, font="-weight bold")

        playerX, playerY = ("Black", "White") if self.playerX.color == "B" else ("White", "Black")
        scoreText = "Player X (%s) Score: %s    VS    Player Y (%s) Score: %s" % (playerX, score[0], playerY, score[1])
        self.canvas.create_text(WIDTH/2, HEIGHT - PADDING/2, anchor="center", text=scoreText)

        for i,row in enumerate(self.board):
            for j,col in enumerate(row):
                self.canvas.grid(row=i,column=j)
                tileColor = "#007E0B" if ((i + j) % 2 == 0) else "#009D0D"

                tileMinX, tileMinY = PADDING + i*self.tileLength, 1.5*PADDING + j*self.tileLength
                tileMaxX, tileMaxY = tileMinX + self.tileLength, tileMinY + self.tileLength

                if i == 0:
                    self.canvas.create_text(tileMinY + self.tileLength/2 - 0.5*PADDING, PADDING*1.25, anchor="center", text=str(j))

                if j == 0:
                    self.canvas.create_text(PADDING*0.75, tileMinX + self.tileLength/2 + 0.5*PADDING, anchor="center", text=str(i))

                self.canvas.create_rectangle(tileMinX, tileMinY, tileMaxX, tileMaxY, outline="black", fill=tileColor)

                pieceMinX, pieceMinY = tileMinX + TILEPADDING, tileMinY + TILEPADDING
                pieceMaxX, pieceMaxY = pieceMinX + self.pieceLength, pieceMinY + self.pieceLength

                if self.board[i][j] != ' ':
                    pieceColor = 'white' if self.board[i][j] == 'W' else 'black'

                    self.canvas.create_oval(pieceMinX, pieceMinY, pieceMaxX, pieceMaxY, fill=pieceColor, tags="oval")

        self.canvas.bind('<Button-1>',lambda e: self.tileClicked(e))

    def tileClicked(self, e):
        if (PADDING <= e.x <= WIDTH - PADDING) and (PADDING <= e.y <= HEIGHT - PADDING):
            i, j = int((e.x - PADDING) / self.tileLength), int((e.y - PADDING) / self.tileLength)

            if self.playerXTurn:
                # Make Player X Move
                print(i, j)
            else:
                # Make Player Y Move
                print(i, j)







