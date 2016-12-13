import MoveUtil 
class OneMoveAI:
    def __init__(self, color):
        self.color = color
        self.opponentColor = 'W' if self.color == 'B' else 'B' 
    
    def evaluationFunction(self, board):
        score = 0
        for row in board:
            for entry in row:
                if entry == self.color:
                    score += 1
                elif entry == self.opponentColor:
                    score -= 1
        return score
        
    def move(self, board, possibleMoves):
        gameTree = MoveUtil.Node(board, self.color, 0 , 1)
        movesAndScores = [(move, self.evaluationFunction(child.board)) for (move, child) in gameTree.children]
        chosenMove = max(movesAndScores, key=lambda x: x[1])[0]
        MoveUtil.updateBoard(board, possibleMoves, chosenMove, self.color)
        