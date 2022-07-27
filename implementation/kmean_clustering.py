
# TODO: Kmean Agorithm
'''
https://www.geeksforgeeks.org/k-means-clustering-introduction/

Initialize k means with random values
For a given number of iterations:
    Iterate through items:
        Find the centroid closest to the item
        Assign item to centroid
        Update centroid
'''
# Import Libraries
from ulab import numpy as np
import sys
import random
import math

# Define data
X = np.array([[100,5], [90,5], [110,5], [97,4], [102,4], [112,4], [92,4], [95,3], [90,3], [100,3],
     [110,5], [100,5], [110,4], [93,3], [107,2], [117,3], [96,2], [105,3], [100,3], [110,3],
     [60,1], [70,1],[40,1], [70,3], [50,1], [80,0],[50,0],[60,1],[60,1],[55,0],
     [40,1], [45,1],[40,0], [55,3], [60,1], [65,0],[70,0],[51,2],[51,1],[48,0]]) #, dtype=np.int16)
# X = np.loadtxt("s1.txt")

# Helper functions
def find_col_minmax(items):
    n = len(items[0]);
    minima = [sys.maxsize for i in range(n)];
    maxima = [-sys.maxsize -1 for i in range(n)];
      
    for item in items:
        for f in range(len(item)):
            if (item[f] < minima[f]):
                minima[f] = item[f];
              
            if (item[f] > maxima[f]):
                maxima[f] = item[f];
  
    return minima,maxima;

# function to count the number of bits in a number n
def count_bits(n):
    # bin(n) returns a binary string representation of n preceded by '0b' in python
    binary = bin(n)
   
    # we did -2 from length of binary string to ignore '0b'
    return len(binary)-2

def random_sample():
    # mantissa = 0x10_0000_0000_0000 | random.getrandbits(52)
    mantissa = 0x10_0000_000 | random.getrandbits(32)
    exponent = -33 #default 53
    x = 0
    while not x:
        x = random.getrandbits(18)
        # print("Count Bits = ", count_bits(x))
        exponent += count_bits(x) - 18
    return math.ldexp(mantissa, exponent)

def uniform(a, b):
        "Get a random number in the range [a, b) or [a, b] depending on rounding."
        return a + (b - a) * (random_sample())

def euclidean_distance(x, y): 
    S = 0; # The sum of the squared differences of the elements 
    for i in range(len(x)): 
        S += math.pow(x[i]-y[i], 2)
  
    #The square root of the sum
    return math.sqrt(S)

# Initailize centroids
def initialize_centroids(items, k, cMin, cMax):
  
    # Initialize means to random numbers between
    # the min and max of each column/feature    
    f = len(items[0]); # number of features
    centroids = [[0 for i in range(f)] for j in range(k)];
      
    for centroid in centroids:
        for i in range(len(centroid)):
  
            # Set value to a random float
            # (adding +-1 to avoid a wide placement of a mean)
            centroid[i] = uniform(cMin[i]+1, cMax[i]-1);
  
    return centroids;

# Update Centroids
def update_centroid(n, centroid, item):
    for i in range(len(centroid)):
        m = centroid[i];
        m = (m*(n-1)+item[i])/float(n);
        centroid[i] = round(m, 3);
      
    return centroid;

# Classify Items
def classify(centroids, item):
  
    # classify item to the mean with minimum distance    
    minimum = sys.maxsize;
    index = -1;
  
    for i in range(len(centroids)):
  
        # Find distance from item to mean
        dis = euclidean_distance(item, centroids[i]);
  
        if (dis < minimum):
            minimum = dis;
            index = i;
      
    return index;

# Find Centroids
def calculate_centroids(k,items,maxIterations=100000):
  
    # Find the minima and maxima for columns
    cMin, cMax = find_col_minmax(items);
      
    # Initialize centroids at random points
    centroids = initialize_centroids(items,k,cMin,cMax);
      
    # Initialize clusters, the array to hold
    # the number of items in a class
    clusterSizes= [0 for i in range(len(centroids))];
  
    # An array to hold the cluster an item is in
    belongsTo = [0 for i in range(len(items))];
  
    # Calculate centroids
    for e in range(maxIterations):
  
        # If no change of cluster occurs, halt
        noChange = True;
        for i in range(len(items)):
  
            item = items[i];
  
            # classify item into a cluster and update the
            # corresponding centroids.        
            index = classify(centroids,item);
  
            clusterSizes[index] += 1;
            cSize = clusterSizes[index];
            centroids[index] = update_centroid(cSize,centroids[index],item);
  
            # Item changed cluster
            if(index != belongsTo[i]):
                noChange = False;
  
            belongsTo[i] = index;
  
        # Nothing changed, return
        if (noChange):
            break;
  
    return centroids;

# Find Clusters
def find_clusters(centroids,items):
    clusters = [[] for i in range(len(centroids))]; # Init clusters
      
    for item in items:
  
        # classify item into a cluster
        index = classify(centroids,item);
  
        # Add item to cluster
        clusters[index].append(item);
  
    return clusters;

#TESTING
# centroids = calculate_centroids(2, X)
# print(f"Centroids = {centroids}")
# clusters = find_clusters(centroids, X)
# # Count each cluster's items
# for i in range(len(clusters)):
#     print(f"Cluster {i} = {len(clusters[i])}")