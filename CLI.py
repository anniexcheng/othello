import Game
from HumanPlayer import HumanPlayer
from RandomMoveAI import RandomMoveAI
from OneMoveAI import OneMoveAI
from MinMaxAI import MinMaxAI
from MinMaxPrunedAI import MinMaxPrunedAI

def choosePlayer(option, color):
    option = int(option)
    if option == 0:
        return HumanPlayer(color)
    elif option == 1:
        return RandomMoveAI(color)
    elif option == 2:
        return OneMoveAI(color)
    elif option == 3:
        return MinMaxAI(color, 3)
    elif option == 4:
        return MinMaxAI(color, 4)
    elif option == 5:
        return MinMaxAI(color, 5)
    elif option == 6:
        return MinMaxAI(color, 6)
    elif option == 7:
        return MinMaxAI(color, 7)
    elif option == 8:
        return MinMaxPrunedAI(color, 3)
    else:
        option = input("Please enter a valid option: ")
        choosePlayer(option)

def othello(N, isExperiment, experimentX, experimentY):
    board, playerXColor, playerYColor, playerXTurn = Game.initializeGame(N, isExperiment)
    
    if not isExperiment:
        print("You can either choose to play as a human or have a bot play")
        print("Please enter your most preferred option") 
        print("Enter 0 for Human")
        print("Enter 1 for AI that moves randomly")
        print("Enter 2 for AI that naively tries to maximize its next turn") 
        print("Enter 3 for AI that uses the Min-Max algorithm looking 3 moves ahead") 
        print("Enter 4 for AI that uses the Min-Max algorithm looking 4 moves ahead") 
        print("Enter 5 for AI that uses the Min-Max algorithm looking 5 moves ahead") 
        print("Enter 6 for AI that uses the Min-Max algorithm looking 6 moves ahead") 
        print("Enter 7 for AI that uses the Min-Max algorithm looking 7 moves ahead") 
        print("Enter 8 for AI that uses the Min-Max Pruning algorithm looking 3 moves ahead") 
        playerX = choosePlayer(input("Enter your option for Player X: "), playerXColor)
        playerY = choosePlayer(input("Enter your option for Player Y: "), playerYColor)
    else: 
        playerX = choosePlayer(experimentX[0], experimentX[1])
        playerY = choosePlayer(experimentY[0], experimentY[1])
    
    return Game.playGame(N, board, playerX, playerY, playerXTurn, isExperiment)
       
if __name__ == '__main__':
    othello(8, False, None, None)
    