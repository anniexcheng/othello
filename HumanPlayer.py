import MoveUtil 
class HumanPlayer:
    def __init__(self, color):
        self.color = color
    
    def move(self, board, possibleMoves):
        moves, chosenMove = None, None

        while True:
            try:
                moves = input("Specify which square you would like to move e.g. 3 5 for (3,5) : ").split(' ')
                chosenMove = (int(moves[0]), int(moves[1]))
            except (IndexError, ValueError):
                print("Invalid Input: Input should be in format 3 5 for (3, 5)")
            else: 
                break

        if chosenMove in possibleMoves:
            MoveUtil.updateBoard(board, possibleMoves, chosenMove, self.color)
        else:
           print("Not a valid move; you can only move in the following squares: ")
           print(list(possibleMoves.keys()))
           self.move(board, possibleMoves)
        