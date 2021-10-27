import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.naive_bayes import *
# from sklearn.naive_bayes import GaussianNB
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.naive_bayes import MultinomialNB




np.random.seed(1)

def equalProb():  # returns 0 or 1 with equal probablity
	if (np.random.random() < 0.5):
		return(0)
	else:
		return(1)

def boundedNormal(bound,stddev):
	rNum = np.random.normal(0,stddev)
	while rNum < -bound or rNum > bound:
		rNum = np.random.normal(0,stddev)
	if (rNum < -2) or (rNum > 2):
		print('returning ' + str(rNum))
	return(rNum)

center1 = 9
center2 = 11
bound = 3
stddev = 1


tuples = []
numTuples = 5000


for i in range(numTuples):
	if (equalProb() == 0):
		candidate = 0

		rNum = boundedNormal(bound,stddev)
		a1 = center1 + rNum

		rNum = boundedNormal(bound,stddev)
		a2 = center1 + rNum

		rNum = boundedNormal(bound,stddev)
		a3 = center1 + rNum

	else:
		candidate = 1

		rNum = boundedNormal(bound,stddev)
		a1 = center2 + rNum

		rNum = boundedNormal(bound,stddev)
		a2 = center2 + rNum

		rNum = boundedNormal(bound,stddev)
		a3 = center2 + rNum


	# atuple = (a1,a2,a5,a3,a4,candidate)
	atuple = (a1,a2,a3,candidate)
	tuples.append(atuple)

	print(atuple)




df = pd.DataFrame(tuples,columns=['a1','a2','a3','candidate'])
print(df)







X = df[ ['a1','a2','a3'] ]
Y = df[ 'candidate']

x_train, x_test, y_train, y_test  = train_test_split( X, Y,  test_size=0.33, random_state=1)
print('len(x_train), len(y_train) = ' + str(len(x_train)) + ',' + str(len(y_train)) )
print('len(x_test), len(y_test) = ' + str(len(x_test)) + ',' + str(len(y_test)) )


clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_train,y_train)
print(clf)
y_predicted = clf.predict(x_test)
print('\nconfusion_matrix from decision tree:')
print(confusion_matrix( y_test, y_predicted ) )
accuracy = accuracy_score(y_test, y_predicted)
recall = recall_score(y_test, y_predicted)
precision = precision_score(y_test, y_predicted)
print('accuracy = ' + str(accuracy))
print('recall = ' + str(recall))
print('precision = ' + str(precision))

model = GaussianNB()
model.fit(x_train,y_train)
gausianNB_predicted = model.predict(x_test)
print('\nconfusion_matrix from Gaussian naive bayes:')
print(confusion_matrix( y_test, gausianNB_predicted ) )
accuracy = accuracy_score(y_test, gausianNB_predicted)
recall = recall_score(y_test, gausianNB_predicted )
precision = precision_score(y_test, gausianNB_predicted)
print('accuracy = ' + str(accuracy))
print('recall = ' + str(recall))
print('precision = ' + str(precision))

model = MultinomialNB()
model.fit(x_train,y_train)
multinomialNB_predicted = model.predict(x_test)
print('\nconfusion_matrix from Multinomial naive bayes:')
print(confusion_matrix( y_test, multinomialNB_predicted ) )
accuracy = accuracy_score(y_test, multinomialNB_predicted)
recall = recall_score(y_test, multinomialNB_predicted )
precision = precision_score(y_test, multinomialNB_predicted)
print('accuracy = ' + str(accuracy))
print('recall = ' + str(recall))
print('precision = ' + str(precision))




# print( df.hist() )

# print( df.hist() )
