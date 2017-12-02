from numpy import *
from matplotlib.pyplot import *
import csv
from scipy.special import gamma
rc('text',usetex = True)

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
excld = 50
dm = 0.01
average = (matrix[::,excld::]).flatten()
bins = arange(0,7.0,dm)
b = 1/mean(average)
"""
figure()
hist(average, bins = bins , normed = 1)
ylabel('Number of agents')
xlabel('Relative wealth (arbitrary currency/amount)')
plot(bins,b*exp(-b*bins))
savefig('l0Histrogram.pdf')

# 5b
figure()
x = sort(average)
y = log10(b*exp(-b*x))
linear = polyfit(x,y,1)
plot(x,y,'.')
plot(x,polyval(linear,x),'r',label = 'f(x)=%.2fx%.2f'%(linear[0],linear[1]))
legend()
savefig('logPlot.png')

#5c
dm = 0.01
figure()
ylabel('Number of agents')
xlabel('Relative wealth (arbitrary currency/amount)')
bins = arange(0,2.5,dm)
matrix2 = getMatrix("0.25l.txt")
matrix3 = getMatrix("0.50l.txt")
matrix4 = getMatrix("0.75l.txt")
matrix5 = getMatrix("0.90l.txt")
y1 = histogram(average, bins = bins , normed = 1)[0]
y2 = histogram(matrix2[::,excld::].flatten(), bins = bins , normed = 1)[0]
y3 = histogram(matrix3[::,excld::].flatten(), bins = bins , normed = 1)[0]
y4 = histogram(matrix4[::,excld::].flatten(), bins = bins , normed = 1)[0]
y5 = histogram(matrix5[::,excld::].flatten(), bins = bins , normed = 1)[0]
x = bins[0:-1]
plot(x,y1, '.',label = "$\lambda = 0.00$")
plot(x,y2, '.',label = "$\lambda = 0.25$")
plot(x,y3, '.',label = "$\lambda = 0.50$")
plot(x,y4, '.',label = "$\lambda = 0.75$")
plot(x,y5, '.',label = "$\lambda = 0.90$")
plot(x,fitting(x,0.00), label = "gibbs distribution")
plot(x,fitting(x,0.25),'b')
plot(x,fitting(x,0.50),'b')
plot(x,fitting(x,0.75),'b')
plot(x,fitting(x,0.90),'b')
legend()
savefig("lamdbaComparisons.pdf")
"""

#5d

dm = 0.01
figure()
ylabel('Number of agents in percent')
xlabel('Relative wealth (arbitrary currency/amount)')
matrix1 = getMatrix("test_0.txt")
matrix2 = getMatrix("test_1.txt")
matrix3 = getMatrix("test_2.txt")
matrix4 = getMatrix("test_3.txt")
mMax = max(matrix4.flatten())
bins = arange(0,mMax,dm)
y1 = histogram(matrix1[::,excld::].flatten(), bins = bins , normed = 100)[0]
y2 = histogram(matrix2[::,excld::].flatten(), bins = bins , normed = 100)[0]
y3 = histogram(matrix3[::,excld::].flatten(), bins = bins , normed = 100)[0]
y4 = histogram(matrix4[::,excld::].flatten(), bins = bins , normed = 100)[0]
x = bins[0:-1]
loglog(x,y1, label = "$\\alpha = 0.5$")
loglog(x,y2, label = "$\\alpha = 1.0$")
loglog(x,y3, label = "$\\alpha = 1.5$")
loglog(x,y4, label = "$\\alpha = 2.0$")
legend()
show()