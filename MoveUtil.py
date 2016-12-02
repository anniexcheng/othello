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