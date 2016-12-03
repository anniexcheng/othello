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
    
if __name__ == '__main__':
    print experiment1()
    
    
    