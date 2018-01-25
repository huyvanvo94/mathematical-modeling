# Import packages
import numpy as np
import matplotlib.pyplot as plt

# Options for Output Data
PlotTrajectories = True				# If False, plots in [Xi,Xj]-plane
OnePlot = True						# If False, plots trajectories separately
#Frame = [1,2]						# Determines frame for [Xi,Xj]-plane plot

# Initial data
#x0 = [1,1]				# Expand matrix to incorporate more variables
t = [0,1]
x = [0,1]
max_steps = 25

# Parameters
a = 1.1
b = 1.3

# Function f(x) in x(t+1) = f(x(t))
# Comment/uncomment to remove/add variables
def f(x,t):
	xout = (1/6.0)*(x[0]-x[1]+t)
	return xout

# Simulate trajectory
for i in range(2,max_steps):
	xtemp = f(x[-2:],t[-2])
	ttemp = t[-1]+1
	t.extend([ttemp])
	x.extend([xtemp])

# Plot results	
if PlotTrajectories:
	print t
	print x
	plt.plot(t,x,'-r*')
#	plt.xlabel('Time Step')
#	plt.legend()
	plt.xlabel('Time Step')
	plt.ylabel('X')
	
plt.show()
