from numpy import *
from matplotlib.pyplot import *
import csv

with open('100_6',"r") as infile:
	lines = infile.readlines()
	m = len(lines) # mcc
	n = len(lines[0].split(",")) # number of agents
	matrix = zeros([m,n])
	for i in range(m):
		for j in range(n):
			matrix[i][j] = (lines[i].split(","))[j]

# 5a
dm = 0.05
agentsFinal = matrix[:,-1]
b = 1/(mean(agentsFinal))
bins = arange(0,max(agentsFinal),dm)
x = zeros(len(bins)-1)
for i in range(m):
	print("loop" + str(i))
	x = x+hist( agentsFinal, bins = bins , normed = 1)[0]

plot(bins,b*exp(-b*bins))
show()

# 5b
#plot(sort(agentsFinal),log10(b*exp(-b*sort(agentsFinal))))
#show()