from sklearn import datasets
from sklearn import svm


iris = datasets.load_iris()
digits = datasets.load_digits()
"""
print(digits.data,"\n")
print(digits.target,"\n")
print(digits.images[0],"\n")
"""
clf = svm.SVC(gamma=0.001,C=100)
clf.fit(digits.data[:-1],digits.target[:-1])
print(clf.predict(digits.data[-1:]))

#------------------------------

clf = svm.SVC()
clf.fit(iris.data,iris.target)
print(clf.predict(iris.data[:3]))

clf.fit(iris.data,iris.target_names[iris.target])
print(clf.predict(iris.data[:3]))

#------------------------------

from sklearn.datasets import load_iris
X,y = load_iris(return_X_y=True)

clf = svm.SVC().set_params(kernel='linear').fit(X,y)
print(clf.predict(iris.data[-3:]))

clf.set_params(kernel='rbf').fit(X,y)

"""
import numpy as np
from sklearn import kernel_approximation

rng = np.random.RandomState(0)
X = rng.rand(10, 2000)
X = np.array(X, dtype='float32')
print(X.dtype)

transformer = kernel_approximation.RBFSampler()
X_new = transformer.fit_transform(X)
print(X_new.dtype)
"""