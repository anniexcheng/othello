from collections import Counter
from CLI import othello
from timeit import Timer

""" Helper Functions """

# Runs an experiment for X trials between two AI bots
def runExperiment(trials, playerB, playerW):
    counter = Counter()
    i = 0
    print("Experiment running...")
    while i < trials:
        winner = othello(8, True, (playerB, 'B'), (playerW, 'W'))
        counter[winner] += 1
        i += 1
    return counter

# Prints the experiment corresponding to the number
def printExperimentResults(number):
    switch = {
        1: experiment1,
        2: experiment2,
        3: experiment3, 
        4: experiment4, 
        5: experiment5,
        6: experiment6,
        7: experiment7,
        8: experiment8,
        9: experiment9,
        10: experiment10,
        11: experiment11,
        12: experiment12,
        13: experiment13,
        14: experiment14,
        100: experiment100,
        1000: experiment1000
    }

    experiment = switch.get(number, "")
    print(experiment())

""" AI Bot Experiments """

# Random (1) vs Random (1)
def experiment1():
    return runExperiment(1000, 1, 1)

# Naive Eval Function (2) vs Random (1)
def experiment2():
    return runExperiment(1000, 2, 1)

# 3 Moves Ahead Min Max (3) vs Random (1)
def experiment3():
    return runExperiment(100, 3, 1)

# 4 Moves Ahead Min Max (4) vs Random (1)
def experiment4():
    return runExperiment(100, 4, 1)

# 5 Moves Ahead Min Max (5) vs Random (1)
def experiment5():
    return runExperiment(100, 5, 1)

# 3 Moves Ahead Min Max (3) vs Naive Eval Function (2)
def experiment6():
    return runExperiment(1, 3, 2)

# 4 Moves Ahead Min Max (4) vs Naive Eval Function (2)
def experiment7():
    return runExperiment(1, 4, 2)

# 5 Moves Ahead Min Max (5) vs Naive Eval Function (2)
def experiment8():
    return runExperiment(1, 5, 2)

# 3 Moves Ahead Min Max Pruning (6) vs Random (1)
def experiment9():
    return runExperiment(100, 6, 1)

# 4 Moves Ahead Min Max Pruning (7) vs Random (1)
def experiment10():
    return runExperiment(100, 7, 1)

# 5 Moves Ahead Min Max Pruning (8) vs Random (1)
def experiment11():
    return runExperiment(100, 8, 1)

# 3 Moves Ahead Min Max Pruning (6) vs Naive Eval Function (2)
def experiment12():
    return runExperiment(1, 6, 2)

# 4 Moves Ahead Min Max Pruning (7) vs Naive Eval Function (2)
def experiment13():
    return runExperiment(1, 7, 2)

# 5 Moves Ahead Min Max Pruning (8) vs Naive Eval Function (2)
def experiment14():
    return runExperiment(1, 8, 2)

# Monte Carlo (100) vs Random (1)
def experiment100():
    return runExperiment(10, 100, 1)

# Simulated Annealing (100) vs Random (1)
def experiment1000():
    return runExperiment(100, 1000, 1)

if __name__ == '__main__':
    time = Timer(lambda: printExperimentResults(1000))
    print("%0.7f" % time.timeit(number=1))
    
