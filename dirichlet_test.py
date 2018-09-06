#Just testing out the dirichlet process clustering

import numpy as np
import sklearn
import matplotlib.pyplot as plt


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

data = np.array(data)
print(data)

p = plt.scatter(data[:,0], data[:,1])
plt.show()

