#hello
from sklearn import tree

#Used for training our tree
#Order is [height(cm),weight(lbs),shoe size(US)]
#height is done numerically without '
#meaning 61 = 6ft 1 in
inputData = [[185,165,10],[160,120,8],[180,160,11],[165,140,10],[150,130,9],
			 [170,135,9],[200,180,13]
			]

#Also used for training
outputData = ['male','female','male','male','female','female','male']

clf = tree.DecisionTreeClassifier()
#create the fit using our data sets
clf = clf.fit(inputData,outputData)

#see how accurate our prediction is
predict = clf.predict([[180,80,10]])

print(predict)