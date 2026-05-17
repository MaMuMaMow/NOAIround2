"""
from sklearn.neighbors import NearestNeighbors
import numpy as np
 
#Ball tree
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
model = NearestNeighbors(n_neighbors=2,algorithm='ball_tree').fit(X)

distance,indi = model.kneighbors(X)

print(distance)
print(indi,"\n")
"""
#KDTree **This one is better.
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KDTree
import numpy as np

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
model1 = NearestNeighbors(algorithm='kd_tree',metric='euclidean',leaf_size=30).fit(X)
query_point = [[-1,-1]]
dis , indi = model1.kneighbors(query_point, n_neighbors=3)

print(dis,"\n")
print(indi,"\n")

model2 = KDTree(X, leaf_size=30, metric='euclidean')
dis , indi = model2.query(query_point,k=3,return_distance=1)

print(dis,"\n\n")
print(indi,"\n\n")
