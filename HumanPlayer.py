import MoveUtil 
class HumanPlayer:
    def __init__(self, color):
        self.color = color
    
    def move(self, board, possibleMoves):
        moves = raw_input("Specify which square you would like to move e.g. 3 5 for (3,5) : ").split(' ')
        chosenMove = (int(moves[0]), int(moves[1]))
        if chosenMove in possibleMoves:
            MoveUtil.updateBoard(board, possibleMoves, chosenMove, self.color)
        else:
           print "Not a valid move; you can only move in the following squares: "
           print possibleMoves.keys()
           self.move(board, possibleMoves)
        