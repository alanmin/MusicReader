#Just testing out the dirichlet process clustering

import numpy as np
import scipy as sp
import sklearn
import matplotlib.pyplot as plt

#Function that determines euclidean distance between two points.
def d(x,y) :
	if(len(x) != len(y)) :
		raise ValueError('In d(x,y): len(x) != len(y)')
	return(np.sqrt(np.sum(np.square(np.subtract(x,y)))))



#TODO
#Metropolis Hastings Sampler
def metropolis_hastings() :
	return None



#TODO
#Gibbs Sampler
def gibbs_sampler() :
	return None



#Initialize three clusters: normals sd 1 centered at 0,0 and 5,5, and 10,10
#10 points each
zero = zip([np.random.normal() for i in range(10)],
	[np.random.normal() for j in range(10)])
zero = [z for z in zero]

five = zip([np.random.normal(5) for i in range(10)],
	[np.random.normal(5) for j in range(10)])
five = [f for f in five]

ten = zip([np.random.normal(10) for i in range(10)],
	[np.random.normal(10) for j in range(10)])
ten = [t for t in ten]

data = zero + five + ten



#Initialize cluster assignments with 30 clusters
#c is a 30 x K matrix, where each row is the format [0, ... , 1, 0, ...., 0]
#	and the row with the 1 is the cluster that the observation belongs to
c = np.identity(30, int)

#Modeling with 0 covariance multivariate normal distributions. 
#Initialize mean to be data
theta = data





data = np.array(data)
print(data)

p = plt.scatter(data[:,0], data[:,1])
plt.show()



