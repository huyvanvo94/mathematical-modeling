# Import packages
import numpy as np
import matplotlib.pyplot as plt

# Options for Output Data
PlotTrajectories = True				# If False, plots in [Xi,Xj]-plane
OnePlot = True					# If False, plots trajectories separately
Frame = [1,2]						# Determines frame for [Xi,Xj]-plane plot

# Initial data
x0 = [[2],[2],[2],[2],[2],[2]]				# Expand array to incorporate more variables
t = [0]
x = x0
max_steps = 5

# Parameters

#				[0.1,0.2,0.7,-1]])				# Expand matrix to incorporate more variables

# Matrix A in x(t+1) = A*x(t)
def f(a,x):
	xout = a*x
	return xout

for j in range(6):

	a = 0.5*j-1.25

	# Simulate trajectory
	for i in range(max_steps):
		if j == 0:
			t.extend([t[i]+1])
		xtemp = f(a,x[j][i])
		x[j].extend([xtemp])
	
	if PlotTrajectories:
		symbol = ''
		if j == 0: symbol = 'k-*'
		elif j == 1: symbol = 'r-o'
		elif j == 2: symbol = 'g-x'
		elif j == 3: symbol = 'b->'
		elif j == 4: symbol = 'c-<'
		elif j == 5: symbol = 'm-^'
		if OnePlot == True:
			plt.plot(t,x[j],symbol, label='A='+str(a))
			plt.xlabel('Time Step')
			plt.ylabel('X')
			plt.legend()
#		else:
#			plt.subplot(6,1,i+1)
#			plt.plot(t,x[j],symbol)
#			plt.ylabel('X' + str(i+1))
#			plt.xlabel('Time Step')
#else:	
#	plt.plot(x[:,Frame[0]-1],x[:,Frame[1]-1],'k-*')	
#	plt.xlabel('X' + str(Frame[0]))
#	plt.ylabel('X' + str(Frame[1]))	
	

plt.show()
