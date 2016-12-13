from copy import deepcopy
from collections import Counter
from RandomMoveAI import RandomMoveAI
import MoveUtil
import Game 

class MonteCarloAI:
    def __init__(self, color):
        self.color = color
        self.opponentColor = 'W' if self.color == 'B' else 'B'

    def move(self, board, possibleMoves):
        moveCoords = list(possibleMoves.keys()) 
        counter = Counter() 
        for moveCoord in moveCoords:
        	for i in range(100):
        		tempBoard = deepcopy(board)
        		MoveUtil.updateBoard(tempBoard, possibleMoves, moveCoord, self.color)
        		winner = Game.playGame(8, tempBoard, RandomMoveAI(self.color), RandomMoveAI(self.opponentColor), False, True)
        		if winner == self.color:
        			counter[moveCoord] += 1 
        chosenMove = counter.most_common(1)[0][0] if len(counter) > 0 else random.choice(moveCoords)
        MoveUtil.updateBoard(board, possibleMoves, chosenMove, self.color)