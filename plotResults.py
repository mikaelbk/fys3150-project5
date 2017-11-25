from numpy import *
from matplotlib.pyplot import *
import csv

with open('20_7',"r") as infile:
	lines = infile.readlines()
	m = len(lines)
	n = len(lines[0].split(","))
	matrix = zeros([m,n])
	for i in range(m):
		for j in range(n):
			matrix[i][j] = (lines[i].split(","))[j]

for i in range(m):
	print(sum(matrix[:,i]/m))
#plot(matrix[:,0],label = "0")
#plot(matrix[:,1],label = "1")
#legend()
#show()