import random, MoveUtil

class RandomMoveAI:
    def __init__(self, color):
        self.color = color
    
    def move(self, board, possibleMoves):
        moveCoords = list(possibleMoves.keys())
        chosenMove = random.choice(moveCoords)
        MoveUtil.updateBoard(board, possibleMoves, chosenMove, self.color)
        