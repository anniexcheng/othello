import random, MoveUtil

class RandomMoveAI:
    def __init__(self, color):
        self.color = color
    
    # returns true if player can move AND makes a valid move; else returns false 
    def move(self, board, possibleMoves):
        moveCoords = possibleMoves.keys()
        chosenMove = random.choice(moveCoords)
        MoveUtil.updateBoard(board, possibleMoves, chosenMove, self.color)
        