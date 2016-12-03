def getCardinalDirections(): 
	return [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]] 

def inBounds(coord):
	return coord[0] >= 0 and coord[0] <= 7 and coord[1] >= 0 and coord[1] <=7

def generatePossibleMoves(board, turn):
	moveResults = {} # map where key: move, value: list of values that would flip
	for i in range(8):
		for j in range(8):
			if board[i][j] != ' ':
				continue
			else:
				capturedSquares = [] 
				for cardinalDirection in getCardinalDirections(): 
					[newX, newY] = [i + cardinalDirection[0], j + cardinalDirection[1]]
					if inBounds([newX, newY]) and board[newX][newY] != ' ' and board[newX][newY] != turn:
						temp = [] 
						while inBounds([newX, newY]) and board[newX][newY] != ' ' and board[newX][newY] != turn:
							temp.append((newX, newY))
							newX += cardinalDirection[0]
							newY += cardinalDirection[1]
						if inBounds([newX, newY]) and board[newX][newY] == turn:
							capturedSquares.extend(temp)
				if len(capturedSquares) != 0:
					moveResults[(i,j)] = capturedSquares 
	return moveResults

def getScore(board, playerXColor, playerYColor, N):
    countX = 0 
    countY = 0 
    for i in range(N):
        for j in range(N):
            if board[i][j] == playerXColor:
                countX += 1
            elif board[i][j] == playerYColor:
                countY += 1
    return (countX, countY)
    
def updateBoard(board, possibleMoves, move, color):
    piecesToBeCaptured = possibleMoves[move]
    for (coordX, coordY) in piecesToBeCaptured:
        board[coordX][coordY] = color
    board[move[0]][move[1]] = color

from copy import deepcopy
class Node:
    def __init__(self, board, color, level, maxDepth):
        self.board = board
        self.color = color
        self.level = level
        self.maxDepth = maxDepth
        self.children = []
        if level < maxDepth: 
          self.populateChildren()
    
    def getOpponentColor(self):
        if self.color == 'B':
            return 'W' 
        else:
            return 'B'
        
    def populateChildren(self):
        possibleMoves = generatePossibleMoves(self.board, self.color)
        nextLevel = self.level + 1
        for possibleMove in possibleMoves:
            tempBoard = deepcopy(self.board)
            updateBoard(tempBoard, possibleMoves, possibleMove, self.color)
            self.children.append((possibleMove, Node(tempBoard, self.getOpponentColor(), nextLevel, self.maxDepth)))
    
    