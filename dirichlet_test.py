#Just testing out the dirichlet process clustering

import numpy as np
import scipy as sp
import sklearn
import matplotlib.pyplot as plt
import random
from scipy.stats import multivariate_normal

ALPHA = 1

#Function that determines euclidean distance between two points.
def d(x,y) :
	if(len(x) != len(y)) :
		raise ValueError('In d(x,y): len(x) != len(y)')
	return(np.sqrt(np.sum(np.square(np.subtract(x,y)))))



#TODO
#Metropolis Hastings Sampler
#x is the x value of the cluster we're trying to assign. Should be a list of lists
	#since this should work for multidimensional data
#xmi stands for x minus i. List of the x values of data points that aren't x
#k is the cluster assignments for each of the xmi. Should be an atomic vector
def assignment(x, xmi, k) :
	unique_clusters = set(list(k.elements()))

	#pick a random uniform r
	r = random.uniform(0,1)

	#This is a running total of the probabilities
	s = 0

	#converts the xmi and k into np arrays
	xminp = np.array(xmi)
	knp = np.array(k)
	for c in unique_clusters : 
		#This gives the elements in group c
		w = np.where(knp == c)

		#This unique_clusters[c] should give us n_k
		if(r < unique_clusters[c]/(len(k) + ALPHA) * 
			multivariate_normal(mean = xminp[w].mean(axis = 0)).pdf(x) ) :
			return(c)
	
	#if not an existing cluster, return a new cluster
	return(c)
		


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


p = plt.scatter(data[:,0], data[:,1], c = ["red"] * 30)
plt.show()



