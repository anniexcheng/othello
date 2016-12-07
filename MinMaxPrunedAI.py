import MoveUtil 
class MinMaxPrunedAI:
    def __init__(self, color, numMovesAhead):
        self.color = color
        self.numMovesAhead = numMovesAhead
        self.opponentColor = 'W' if self.color == 'B' else 'B'
        self.pointMatrix =  [ [48,   6,  6,  6,  6,  6,   6, 48,], 
           [ 6, -24, -4, -4, -4, -4, -24,  6,], 
           [ 6,  -4,  1,  1,  1,  1,  -4,  6,], 
           [ 6,  -4,  1,  1,  1,  1,  -4,  6,], 
           [ 6,  -4,  1,  1,  1,  1,  -4,  6,], 
           [ 6,  -4,  1,  1,  1,  1,  -4,  6,], 
           [ 6, -24, -4, -4, -4, -4, -24,  6,], 
           [48,   6,  6,  6,  6,  6,   6, 48,],]
    
    def evaluationFunction(self, board):
        score = 0
        opponentScore = 0 
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == self.color: 
                    score += self.pointMatrix[i][j]
        return score
    
    def minMax(self, node, alpha, beta):
        if node.level == node.maxDepth: 
            score = self.evaluationFunction(node.board)
            return (None, (score, score)) 
        elif len(node.children) == 0:
            (playerScore, opponentScore) = MoveUtil.getScore(node.board, self.color, self.opponentColor, 8)
            if playerScore > opponentScore: 
                return (None, (10000000, 10000000)) 
            else:
                return (None, (-1000000, -1000000))  
              
        moveToTake = None 
        for (move, childNode) in node.children:
            if node.level % 2 == 0:
                tempAlpha = self.minMax(childNode, alpha, beta)[1][1] 
                if tempAlpha > beta: # pruning
                    return (moveToTake, (alpha, beta))  
                if tempAlpha > alpha:
                    alpha = tempAlpha 
                    moveToTake = move 
            else: 
                tempBeta = self.minMax(childNode, alpha, beta)[1][0] 
                if tempBeta < alpha:
                    return (moveToTake, (alpha, beta))  
                if tempBeta < beta:
                    beta = tempBeta
                    moveToTake = move 
          
            if alpha == beta:
                return (moveToTake, (alpha, beta)) if node.level != 0 else moveToTake
          
        if node.level == 0:
            return moveToTake
        else:
            return (moveToTake, (alpha, beta)) 

    def move(self, board, possibleMoves):
        gameTree = MoveUtil.Node(board, self.color, 0, self.numMovesAhead)
        chosenMove = self.minMax(gameTree, float("-inf"), float("inf"))
        MoveUtil.updateBoard(board, possibleMoves, chosenMove, self.color)