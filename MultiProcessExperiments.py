from multiprocessing import Process
import Experiments
from timeit import Timer

def main():
	processes = [] 
	for i in range(2):
		p = Process(target=Experiments.printExperimentResults, args=(1000,))
		p.start()
		processes.append(p)
	for p in processes:
		p.join()

if __name__ == '__main__':
	timer = Timer(lambda: main())
	print("%0.7f" % timer.timeit(number=1))

	  


