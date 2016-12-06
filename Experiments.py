from collections import Counter
from CLI import othello

""" Helper Functions """

# Runs an experiment for X trials between two AI bots
def runExperiment(trials, playerB, playerW):
    counter = Counter()
    i = 0
    print "Experiment running..."
    while i < trials:
        winner = othello(8, True, (playerB, 'B'), (playerW, 'W'))
        counter[winner] += 1
        i += 1
    return counter

# Prints the number of e
def printExperimentResults(number):
    switch = {
        1: experiment1,
        2: experiment2,
        3: experiment3, 
        4: experiment4, 
        5: experiment5,
        6: experiment6,
        7: experiment7
    }

    experiment = switch.get(number, "")
    print experiment()

""" AI Bot Experiments """

# Random (1) vs Random (1)
def experiment1():
    return runExperiment(10000, 1, 1)

# One Move Naive Eval Function (2) vs Random (1)
def experiment2():
    return runExperiment(10000, 2, 1)

# 3 Moves Ahead Min Max (3) vs Random (1)
def experiment3():
    return runExperiment(10000, 3, 1)

# 4 Moves Ahead Min Max (4) vs Random (1)
def experiment4():
    return runExperiment(10000, 4, 1)

# 5 Moves Ahead Min Max (5) vs Random (1)
def experiment5():
    return runExperiment(10000, 5, 1)

# 6 Moves Ahead Min Max (6) vs Random (1)
def experiment6():
    return runExperiment(10000, 6, 1)

# 7 Moves Ahead Min Max (7) vs Random (1)
def experiment7():
    return runExperiment(10000, 7, 1)

if __name__ == '__main__':
    printExperimentResults(1)
    