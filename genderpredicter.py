#hello
from sklearn import tree

inputData = [[200,80,41],[140,67,32],[190,89,40],[195,80,43],[150,65,35]
			]

outputData = ['male','female','male','male','female']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(inputData,outputData)

predict = clf.predict([[180,70,43]])

print(predict)