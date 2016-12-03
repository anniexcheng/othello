from MoveUtil import generatePossibleMoves, getScore, Node

def initializeBoard(N):
  board = []
  for x in range(N):
    board.append([' '] * N)

  board[3][3] = 'W'
  board[4][4] = 'W'
  board[3][4] = 'B'
  board[4][3] = 'B'
  return board 

def drawBoard(board, N):
     HLINE = '  +---+---+---+---+---+---+---+---+'
     VLINE = '  |   |   |   |   |   |   |   |   |'

     print('    0   1   2   3   4   5   6   7')
     print(HLINE)
     for y in range(N):
         print(VLINE)
         print y,
         for x in range(N):
             print '| %s' % (board[x][y]),
         print('|')
         print(VLINE)
         print(HLINE)

# Initializes the game by setting up the board and determining the color
# corresponding to each player
def initializeGame(N):
    playerXColor = raw_input("Choose whether you want to be B or W (B goes first): ")
    playerYColor = 'B' if playerXColor == 'W' else 'W'
    print "Player X is %s" % playerXColor
    print "Player Y is %s" % playerYColor
    playerXTurn = True if playerXColor == 'B' else False 
    print "Whoever is B will go first"
    return initializeBoard(N), playerXColor, playerYColor, playerXTurn 

# Given a board and the color associated with the player, checks if
# the player can make a valid move; it will return a boolean value 
# of whether it can move or not as the first of the pair, and the
# possibleMoves as second of the pair
def canMove(board, color):
    possibleMoves = generatePossibleMoves(board, color)
    if len(possibleMoves.keys()) == 0:
        return False, possibleMoves
    else:
        return True, possibleMoves
# Given the color associated with the two players and the board,
# determines who has won 
def endGame(playerXColor, playerYColor, board, N):
    counts = getScore(board, playerXColor, playerYColor, N)
    print "Player X has a score of %s" % counts[0]
    print "Player Y has a score of %s" % counts[1]

    playerXWon = True if counts[0] > counts[1] else False
    print "%s has won!" % ("Player X" if playerXWon else "Player Y")
    if playerXWon:
        return playerXColor
    else:
        return playerYColor
    
def playGame(N, board, playerX, playerY, playerXTurn):
    while True:
        drawBoard(board, N)
        playerXCanMove, playerXMoves = canMove(board, playerX.color)
        playerYCanMove, playerYMoves = canMove(board, playerY.color)
        if playerXTurn:
            print "Player X's turn!"
        else:
            print "Player Y's turn!" 
        
        currentScore = getScore(board, playerX.color, playerY.color, N)
        print "Current score: Player X: %s vs Player Y: %s" % (currentScore[0], currentScore[1])
            
        if not (playerXCanMove or playerYCanMove):
            return endGame(playerX.color, playerY.color, board, N)
        elif playerXTurn and playerXCanMove:
            playerX.move(board, playerXMoves)
            playerXTurn = False
        elif not playerXTurn and playerYCanMove:
            playerY.move(board, playerYMoves)
            playerXTurn = True
        elif not playerXTurn and not playerYCanMove:
            print "Player Y cannot move; Player X will move this turn" 
            playerX.move(board, playerXMoves)
        elif playerXTurn and not playerXCanMove:
            print "Player X cannot move; Player Y will move this turn"
            playerY.move(board, playerYMoves)
            
    