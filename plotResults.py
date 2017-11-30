from numpy import *
from matplotlib.pyplot import *
import csv
from scipy.special import gamma

def getMatrix(filename):
	with open(filename,"r") as infile:
		lines = infile.readlines()
		m = len(lines) # mcc
		n = len(lines[0].split(",")) # number of agents
		matrix = zeros([m,n])
		for i in range(m):
			for j in range(n):
				matrix[i][j] = (lines[i].split(","))[j]
		return matrix

def avgValsHist(matrix, exclusions, bins): #not yet finished
	average = (matrix[::,exclusions::]).flatten()
	if(len(bins)==1):
		bins = arange(0,max(average),bins[0])
	return 0

def fitting(x,lam):
	n = 1 + 3*lam/(1-lam)
	an = n**n/gamma(n)
	return an*x**(n-1)*exp(-n*x)

matrix = getMatrix("0.00l.txt")

# 5a
excld = 1
dm = 0.05
average = (matrix[::,excld::]).flatten()
bins = arange(0,max(average),dm,)
b = 1/mean(average)
"""
hist(average, bins = bins , normed = 1)
plot(bins,b*exp(-b*bins))
show()

# 5b
x = sort(average)
y = log10(b*exp(-b*x))
linear = polyfit(x,y,1)
plot(x,y,'.')
plot(x,polyval(linear,x),'r',label = 'f(x)=%.2fx%.2f'%(linear[0],linear[1]))
legend()
show()
"""

#5c
matrix2 = getMatrix("0.25l.txt")
matrix3 = getMatrix("0.50l.txt")
matrix4 = getMatrix("0.75l.txt")
matrix5 = getMatrix("0.90l.txt")
y1 = histogram(average, bins = bins , normed = 1)[0]
y2 = histogram(matrix2[::,excld::], bins = bins , normed = 1)[0]
y3 = histogram(matrix3[::,excld::], bins = bins , normed = 1)[0]
y4 = histogram(matrix4[::,excld::], bins = bins , normed = 1)[0]
y5 = histogram(matrix5[::,excld::], bins = bins , normed = 1)[0]
x = bins[0:-1]
plot(x,b*exp(-b*x), label = "gibbs distribution")
plot(x,y1, '.',label = "l=0")
plot(x,y2, '.',label = "l=0.25")
plot(x,y3, '.',label = "l=0.50")
plot(x,y4, '.',label = "l=0.75")
plot(x,y4, '.',label = "l=0.90")
legend()
show()
