import Game
from HumanPlayer import HumanPlayer
from RandomMoveAI import RandomMoveAI
from OneMoveAI import OneMoveAI

def choosePlayer(option, color):
    option = int(option)
    if option == 0:
        return HumanPlayer(color)
    elif option == 1:
        return RandomMoveAI(color)
    elif option == 2:
        return OneMoveAI(color)
    else:
        option = raw_input("Please enter a valid option: ")
        choosePlayer(option)

def othello(N, isExperiment, experimentX, experimentY):
    board, playerXColor, playerYColor, playerXTurn = Game.initializeGame(N, isExperiment)
    
    if not isExperiment:
        print "You can either choose to play as a human or have a bot play"
        print "Please enter your most preferred option" 
        print "Enter 0 for Human"
        print "Enter 1 for AI that moves randomly"
        playerX = choosePlayer(raw_input("Enter your option for Player X: "), playerXColor)
        playerY = choosePlayer(raw_input("Enter your option for Player Y: "), playerYColor)
    else: 
        playerX = choosePlayer(experimentX[0], experimentX[1])
        playerY = choosePlayer(experimentY[0], experimentY[1])
    
    return Game.playGame(N, board, playerX, playerY, playerXTurn, isExperiment)
       
if __name__ == '__main__':
    othello(8, False, None, None)
    