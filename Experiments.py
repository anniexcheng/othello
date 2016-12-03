from collections import Counter
from CLI import othello

if __name__ == '__main__':
    counter = Counter()
    i = 0
    print "Experiment running..."
    while i < 10000:
        winner = othello(8, True, (1, 'B'), (1, 'W'))
        counter[winner] += 1
        i += 1
    print counter
    
    
    