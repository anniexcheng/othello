from collections import Counter
from CLI import othello

# Random vs Random
# Trial 1: Counter({'W': 5496, 'B': 4504})
def experiment1():
    counter = Counter()
    i = 0
    print "Experiment running..."
    while i < 10000:
        winner = othello(8, True, (1, 'B'), (1, 'W'))
        counter[winner] += 1
        i += 1
    return counter

# One Move, Naive Eval Function vs Random
# Trial 1: Counter({'B': 5808, 'W': 4192}) 
# Trial 2: Counter({'B': 5887, 'W': 4113})
def experiment2():
    counter = Counter()
    i = 0
    print "Experiment running..."
    while i < 10000:
        winner = othello(8, True, (2, 'B'), (1, 'W'))
        counter[winner] += 1
        i += 1
    return counter
    
if __name__ == '__main__':
    #print experiment1()
    print experiment2()
    
    
    