class HumanPlayer:
    def __init__(self, color):
        self.color = color
    
    # returns true if player can move AND makes a valid move; else returns false 
    def move(self, board, possibleMoves):
        moves = raw_input("Specify which square you would like to move e.g. 3 5 for (3,5) : ").split(' ')
        moveXCoord, moveYCoord = int(moves[0]), int(moves[1])
        if (moveXCoord, moveYCoord) in possibleMoves:
            piecesToBeCaptured = possibleMoves[(moveXCoord, moveYCoord)]
            for (coordX, coordY) in piecesToBeCaptured:
                board[coordX][coordY] = self.color
            board[moveXCoord][moveYCoord] = self.color
        else:
           print "Not a valid move; you can only move in the following squares: "
           print possibleMoves.keys()
           self.move(board, possibleMoves)
        