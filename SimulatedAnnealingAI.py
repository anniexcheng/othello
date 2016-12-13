from copy import deepcopy
from random import random, choice
from math import exp 
import MoveUtil 
class SimulatedAnnealingAI:
    def __init__(self, color):
        self.color = color
        self.opponentColor = 'W' if self.color == 'B' else 'B'
        self.pointMatrix = MoveUtil.getPointMatrix() 
        self.temperature = 1000
    
    def evaluationFunction(self, board):
        score = 0
        opponentScore = 0 
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == self.color: 
                    score += self.pointMatrix[i][j]
        return score
    
    def move(self, board, possibleMoves):
        moveCoords = list(possibleMoves.keys())
        currentScore = self.evaluationFunction(board)
        moveToScore = {}
        bestMove = None 
        for moveCoord in moveCoords:
            tempBoard = deepcopy(board)
            MoveUtil.updateBoard(tempBoard, possibleMoves, moveCoord, self.color)
            tempScore = self.evaluationFunction(tempBoard)
            moveToScore[moveCoord] = tempScore - currentScore 
            if bestMove == None or moveToScore[bestMove] < moveToScore[moveCoord]:
                bestMove = moveCoord 

        chosenMove = choice(moveCoords) 
        if moveToScore[chosenMove] <= 0:
             prob = exp(moveToScore[chosenMove] / self.temperature)
             if random() > prob:
                chosenMove = bestMove

        MoveUtil.updateBoard(board, possibleMoves, chosenMove, self.color)
        self.temperature *= 0.5
