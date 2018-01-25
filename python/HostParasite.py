# Import packages
import numpy as np
import matplotlib.pyplot as plt


# Initial data
x = [[5.0]]
x.append([1.0])
#x.append([1])
#x.append([0])
#x.append([0])
#x.append([0])						# Expand array to incorporate more variables
t = [0]
max_steps = 25

# Parameters
a = 3.0

# Define column vector
def column(A,i):
	return [row[i] for row in A]

# Define matrix multiplication
def multiply(A,x):
	return [sum([A[i][j]*x[j] for j in range(len(x))]) for i in range(len(A[0]))]

# Function f(x) in x(t+1) = f(x(t))
# Comment/uncomment to remove/add variables
def f(x):
	H = x[0]
	P = x[1]
	Hout = 2*H/(1.0+P)
	Pout = a*P/(1.0+P/H)
#	xout[2] = np.sin(x[0,1]-x[0,2])
#	xout[3] = np.cos(x[0,0]+np.exp(x[0,3]))
#	xout[4] = np.sin(x[0,0]+x[0,5])
#	xout[5] = x[0,4]-x[0,5]
	return [Hout,Pout]
	
# Simulate trajectory
for i in range(max_steps):
	xtemp = f(column(x,i))
	t.extend([t[i]+1])
	for i in range(len(x)):
		x[i].extend([xtemp[i]])

# Display numerical values of trajectory

for i in range(len(x)):
	print 'X' + str(i+1) + '= ' + str(x[i])
		
# Plot results	
plt.plot(t,x[0],'k-*', label='Hosts')
plt.plot(t,x[1],'r-o', label='Parasite')
plt.xlabel('Time Step')
plt.legend()
plt.title('alpha = 5')
	
plt.show()
