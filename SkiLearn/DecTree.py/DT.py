from sklearn import tree

X = [[0,0],[1,1]]
Y = [0,1]

model = tree.DecisionTreeClassifier().fit(X,Y)
print(model.predict([[2,2],[-1,-1]]))