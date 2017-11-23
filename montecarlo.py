# this program illustrates why python will be too slow in this project

from numpy import *
N = 500
transactions = int(1E6)
experiments = int(1E3)
m0 = 50


agents = m0*ones(N)
agentsThroughTime = ndarray([N,experiments])

def transaction(i,j):
	rand = random.random()
	return rand*(i+j), (1-rand)*(i+j)

for i in range(experiments):
	print("cycle # %d" % (i))
	for j in range(transactions):
		a = random.random()
		b = random.random()