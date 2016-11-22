
def initializeBoard():
  board = []
  for x in range(8):
    board.append([' '] * 8)

  board[3][3] = 'W'
  board[4][4] = 'W'
  board[3][4] = 'B'
  board[4][3] = 'B'
  return board 

def drawBoard(board):
     HLINE = '  +---+---+---+---+---+---+---+---+'
     VLINE = '  |   |   |   |   |   |   |   |   |'

     print('    0   1   2   3   4   5   6   7')
     print(HLINE)
     for y in range(8):
         print(VLINE)
         print y,
         for x in range(8):
             print '| %s' % (board[x][y]),
         print('|')
         print(VLINE)
         print(HLINE)

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

board = initializeBoard() 
drawBoard(board)
player = raw_input("Choose whether you want to be B or W (B goes first): ")
opponent = 'B' if player == 'W' else 'B'
print "Your opponenet is %s" % opponent 
print player 
playerTurn = True if player == 'B' else False 
print generatePossibleMoves(board, player)
while True: 
	if playerTurn: 
		possibleMoves = generatePossibleMoves(board, player)
		x, y = raw_input("Specify which square you would like to move e.g. 3 5 for (3,5) : ")
		print x, y 





