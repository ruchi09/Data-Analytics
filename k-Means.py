import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import random as r


def readMatrix(file):
    fd = open(file, 'r')
    x = list()
    y = list()
    for itemset in fd:
		a=list(itemset.strip().split(","))
		# print a
		x.append(a[1:] )
		y.append(a[0])
    return x,y


def print_list(l,n):
	count=0
	for i in l:
		print i,"    ",
		count+=1
		if count>=n:
			print "\n"
			count=0


if __name__ == "__main__":


	#Preparing data for processing
	X, flight_names =readMatrix("flight.csv")
	X= np.array(X)



	# Plot before clustering
	plt.scatter(X[:,0],X[:,1],label='True Position')


	#Perform clustering for a given number of clusters
	kmeans = KMeans(n_clusters=3)
	kmeans.fit(X)


	#Print the centroids for the clusters formed
	print "\n\n-----------------------------------------------------------------------------------------------------------------"
	print "                                    CLUSTER CENTROIDS"
	print "-----------------------------------------------------------------------------------------------------------------\n"
	print (kmeans.cluster_centers_)


	#Print the labels/cluster numbers the data belongs to
	c0 =list()
	c1=list()
	c2=list()
	for i in range(0,len(kmeans.labels_)):
		if kmeans.labels_[i]==0:
			c0.append(flight_names[i])
		elif kmeans.labels_[i]==1:
			c1.append(flight_names[i])
		else:
			c2.append(flight_names[i])


	print "\n\n\n-----------------------------------------------------------------------------------------------------------------"
	print "                                    CLUSTER FORMED"
	print "-----------------------------------------------------------------------------------------------------------------\n"

	print "\n\n Cluster 0:\n"
	print_list(c0,10)

	print "\n\n\n\n Cluster 1:\n"
	print_list(c1,10)

	print "\n\n\n\n Cluster 2:\n"
	print_list(c2,10)

	print "\n"

	# Data after clustering
	plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap='rainbow')
