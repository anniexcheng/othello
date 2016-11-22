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
playerA = raw_input("Choose whether you want to be B or W (B goes first): ")
playerB = 'B' if playerA == 'W' else 'W'
print "Player B is %s" % playerB 
playerATurn = True if playerA == 'B' else False 
print "Whoever is B will go first"
 
while True: 
    possibleMovesPlayerA = generatePossibleMoves(board, playerA)
    possibleMovesPlayerB = generatePossibleMoves(board, playerB)
    if len(possibleMovesPlayerA.keys()) == 0 and len(possibleMovesPlayerB.keys()) == 0:
        break 
    
    playerToMove = playerA if playerATurn else playerB
    possibleMoves = possibleMovesPlayerA if playerATurn else possibleMovesPlayerB
    if len(possibleMoves.keys()) == 0:
            print "Nowhere to move; opponent's turn!" 
            playerTurn = not playerTurn
            continue
    moves = raw_input("Specify which square you would like to move e.g. 3 5 for (3,5) : ").split(' ')
    moveXCoord, moveYCoord = int(moves[0]), int(moves[1])
    if (moveXCoord, moveYCoord) in possibleMoves:
        for (coordX, coordY) in possibleMoves[(moveXCoord, moveYCoord)]:
            board[coordX][coordY] = playerToMove 
        board[moveXCoord][moveYCoord] = playerToMove
        playerATurn = not playerATurn
    else:
        print "Not a valid move; you can only move in the following squares: "
        print possibleMoves.keys()
    
    drawBoard(board)

countA = 0 
countB = 0 
for i in range(8):
    for j in range(8):
        if board[i][j] == playerA:
            countA += 1
        elif board[i][j] == playerB:
            countB += 1

print "Player A has a score of %s" % countA
print "Player B has a score of %s" % countB
print "%s has won!" % ("Player A" if countA > countB else "Player B")

            





