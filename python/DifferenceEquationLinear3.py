# Import packages
import numpy as np
import matplotlib.pyplot as plt

# Options for Output Data
DisplayNumerical = True
PlotTrajectories = True				# If False, plots in [Xi,Xj]-plane
OnePlot = True						# If False, plots trajectories separately
Frame = [1,2]						# Determines frame for [Xi,Xj]-plane plot

# Initial data
x = [[1]]
x.append([-1])
#x.append([1])
#x.append([0])
#x.append([0])
#x.append([0])						# Expand array to incorporate more variables
t = [0]
max_steps = 25

# Parameters
a = 1
A = [	[1.0/2.0,-1.0/2.0],
		[5.0/4.0,1]]				# Expand matrix to incorporate more variables, must be square
	
# Define column vector
def column(A,i):
	return [row[i] for row in A]

# Define matrix multiplication
def multiply(A,x):
	return [sum([A[i][j]*x[j] for j in range(len(x))]) for i in range(len(A[0]))]

# Matrix A in x(t+1) = A*x(t)
def f(x):
	return multiply(A,x)

# Simulate trajectory
for i in range(max_steps):
	xtemp = f(column(x,i))
	t.extend([t[i]+1])
	for i in range(len(x)):
		x[i].extend([xtemp[i]])

# Display numerical values of trajectory
if DisplayNumerical == True:
	for i in range(len(x)):
		print 'X' + str(i+1) + '= ' + str(x[i])
		
# Plot results	
if PlotTrajectories:
	for i in range(len(x)):
		symbol = ''
		if i == 0: symbol = 'k-*'
		elif i == 1: symbol = 'r-o'
		elif i == 2: symbol = 'g-x'
		elif i == 3: symbol = 'b->'
		elif i == 4: symbol = 'c-<'
		elif i == 5: symbol = 'm-^'
		if OnePlot == True:
			plt.plot(t,x[i],symbol, label='X'+str(i))
			plt.xlabel('Time Step')
			plt.legend()
		else:
			plt.subplot(len(x),1,i+1)
			plt.plot(t,x[i],symbol)
			plt.ylabel('X' + str(i+1))
			plt.xlabel('Time Step')
else:	
	plt.plot(x[Frame[0]-1],x[Frame[1]-1],'k-*')
	plt.xlabel('X' + str(Frame[0]))
	plt.ylabel('X' + str(Frame[1]))	
	
plt.show()
