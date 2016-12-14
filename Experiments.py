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
        15: experiment15,
        16: experiment16,
        100: experiment100,
        101: experiment101,
        102: experiment102,
        103: experiment103,
        104: experiment104,
        1000: experiment1000,
        1001: experiment1001,
        1002: experiment1002,
        1003: experiment1003,
        1004: experiment1004,
        1005: experiment1005,
        1006: experiment1006,
        1007: experiment1007,
        1008: experiment1008,
        1009: experiment1009,
        1010: experiment1010,
        1011: experiment1011
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

# 6 Moves Ahead Min Max (6) vs Naive Eval Function (2)
def experiment9():
    return runExperiment(1, 6, 2)

# 3 Moves Ahead Min Max Pruning (7) vs Random (1)
def experiment10():
    return runExperiment(100, 7, 1)

# 4 Moves Ahead Min Max Pruning (8) vs Random (1)
def experiment11():
    return runExperiment(100, 8, 1)

# 5 Moves Ahead Min Max Pruning (9) vs Random (1)
def experiment12():
    return runExperiment(100, 9, 1)

# 3 Moves Ahead Min Max Pruning (7) vs Naive Eval Function (2)
def experiment13():
    return runExperiment(1, 7, 2)

# 4 Moves Ahead Min Max Pruning (8) vs Naive Eval Function (2)
def experiment14():
    return runExperiment(1, 8, 2)

# 5 Moves Ahead Min Max Pruning (9) vs Naive Eval Function (2)
def experiment15():
    return runExperiment(1, 9, 2)

# 6 Moves Ahead Min Max Pruning (10) vs Naive Eval Function (2)
def experiment16():
    return runExperiment(1, 10, 2)

# Monte Carlo (100) vs Random (1)
def experiment100():
    return runExperiment(10, 100, 1)

# Monte Carlo (100) vs Naive (2)
def experiment101():
    return runExperiment(10, 100, 2)

# Monte Carlo (100) vs 3 Moves Ahead MinMax (7)
def experiment102():
    return runExperiment(10, 100, 7)

# Monte Carlo (100) vs 4 Moves Ahead MinMax (8)
def experiment103():
    return runExperiment(10, 100, 8)

# Monte Carlo (100) vs 5 Moves Ahead MinMax (9)
def experiment104():
    return runExperiment(10, 100, 9)

# Simulated Annealing (1000) vs 3 Moves Ahead MinMax Pruned (7)
def experiment1000():
    return runExperiment(100, 1000, 7)

# Simulated Annealing (1000) vs 4 Moves Ahead MinMax Pruned (8)
def experiment1001():
    return runExperiment(5, 1000, 8)

# Simulated Annealing (1000) vs 5 Moves Ahead MinMax Pruned (9)
def experiment1002():
    return runExperiment(10, 1000, 9)

# 3 Moves Ahead MinMax Pruned (7) vs Simulated Annealing (1000)
def experiment1003():
    return runExperiment(100, 7, 1000)

# 4 Moves Ahead MinMax Pruned (8) vs Simulated Annealing (1000)
def experiment1004():
    return runExperiment(100, 8, 1000)

# 5 Moves Ahead MinMax Pruned (9) vs Simulated Annealing (1000)
def experiment1005():
    return runExperiment(100, 9, 1000)

# Simulated Annealing (1000) vs Random (1)
def experiment1006():
    return runExperiment(1000, 1000, 1)

# Random (1) vs Simulated Annealing (1000)
def experiment1007():
    return runExperiment(1000, 1, 1000)

# Simulated Annealing (1000) vs Naive Eval (2)
def experiment1008():
    return runExperiment(1000, 1000, 2)

# Naive Eval (2) vs Simulated Annealing (1000)
def experiment1009():
    return runExperiment(1000, 2, 1000)

def experiment1010():
    return runExperiment(1000, 1000, 1001)

def experiment1011():
    return runExperiment(1000, 1001, 1000)

if __name__ == '__main__':
    time = Timer(lambda: printExperimentResults(103))
    print("%0.7f" % time.timeit(number=1))
    
