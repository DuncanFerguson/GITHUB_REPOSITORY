import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.naive_bayes import *
# from sklearn.naive_bayes import GaussianNB
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.naive_bayes import MultinomialNB

# probInGroup = 0.8  # probability that rule predicts which candidate vs random, 
probInGroup = 1.0  # probability that rule predicts which candidate vs random, 

# 1.0 means rules exactly predict, 0.0 means completely random

# feature vector = age, education-level, minoritized, pro-choice, gender
# where education level (0, 1, 2, 3 where 1 == HS, 2 == some college, 3 == bachelors+)
# pro-choice vs pro-life (0 means not pro-choice, i.e pro-life, 1 means yes pro-choice)
# minoritized = 0 means not identify as member of minoritized population
# gender:  0 means identify female, 1 means male, 2 means neither

# Candidate A with 90% probability
# (age <= 30) && (education = 2 or 3 )
# (age > 30) && (education = 2 or 3 ) & (gender = 0)
# (minoritized =1)  and (gender == 0 or 2)
# (minoritized =1)  and (pro-choice = 1)
# (gender = 2)  

# Candidate B
# (pro choice = 0) && (education level < 3)
# (minoritized =0) && (50 < age > 70) && (education level < 3)
# (minoritized =0) && (age > 70)


def equalProb():  # returns 0 or 1 with equal probablity
	if (np.random.random() < 0.5):
		return(0)
	else:
		return(1)

np.random.seed(1)   # make reproducible
tuples = []
# numTuples = 30
numTuples = 20000
numRandomlyChosen = 0
for i in range(numTuples):
	age = np.random.randint(18,100)
	education = np.random.randint(0,3)
	rNum = np.random.random()
	if (rNum < 0.37):
		minoritized = 0
	else:
		minoritized = 1
	rNum = np.random.random()
	if (rNum < 0.4):
		prochoice = 0
	else:
		prochoice = 1
	rNum = np.random.random()
	if (rNum < 0.02):
		gender = 2
	elif (np.random.random() < 0.5):
		gender = 1
	else:
		gender = 0

	# candidate = -1
	# now assign who they are likely to vote for
	if ((age <= 30) and (education == 2 or education == 3)):
		if (np.random.random() < probInGroup):
			candidate = 0
		else:
			candidate = equalProb()
	elif ((age > 30) and (education == 2 or education == 3) and (gender == 0)):
		if (np.random.random() < probInGroup):
			candidate = 0
		else:
			candidate = equalProb()
	elif( (minoritized == 1) and (gender == 0 or gender == 2)):
		if (np.random.random() < probInGroup):
			candidate = 0
		else:
			candidate = equalProb()
	elif( (minoritized == 1) and (prochoice == 1) ):
		if (np.random.random() < probInGroup):
			candidate = 0
		else:
			candidate = equalProb()
	elif (gender == 2):
		if (np.random.random() < probInGroup):
			candidate = 0
		else:
			candidate = equalProb()
	elif ( (prochoice == 0) and (education < 3)):
		if (np.random.random() < probInGroup):
			candidate = 1
		else:
			candidate = equalProb()
	elif ( (minoritized == 0) and (age >= 50) and (age < 70) and (education < 3)):
		if (np.random.random() < probInGroup):
			candidate = 1
		else:
			candidate = equalProb()
	elif ( (minoritized == 0) and (age > 70)):
		if (np.random.random() < probInGroup):
			candidate = 1
		else:
			candidate = equalProb()
	else:  # equal probability
		numRandomlyChosen += 1
		if (np.random.random() < 0.5): 
			candidate = 1
		else:
			candidate = 0
		candidate = -1  # going to remove all those not in a class

	if (candidate > -1):   # if in one of the rule groups add it, else skip
		atuple = (age, education, minoritized, prochoice, gender, candidate)
		tuples.append(atuple)

	# print(atuple)


df = pd.DataFrame(tuples,columns=['age','education','minoritized','prochoice','gender','candidate'])
print(df)

X = df[ ['age','education','minoritized','prochoice','gender'] ]
Y = df[ 'candidate']

x_train, x_test, y_train, y_test  = train_test_split( X, Y,  test_size=0.33, random_state=1)
print('len(x_train), len(y_train) = ' + str(len(x_train)) + ',' + str(len(y_train)) )
print('len(x_test), len(y_test) = ' + str(len(x_test)) + ',' + str(len(y_test)) )
print('x_test = ')
print(x_test)
print('y_test = ')
print(y_test)


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

'''
# data needs to be in categories {0,1,2..} for this to work properly
model = CategoricalNB()
model.fit(x_train,y_train)
categoricalNB_predicted = model.predict(x_test)
print('\nconfusion_matrix from CategoricalNB naive bayes:')
print(confusion_matrix( y_test, categoricalNB_predicted ) )
accuracy = accuracy_score(y_test, categoricalNB_predicted)
recall = recall_score(y_test, categoricalNB_predicted )
precision = precision_score(y_test, categoricalNB_predicted)
print('accuracy = ' + str(accuracy))
print('recall = ' + str(recall))
print('precision = ' + str(precision))
'''



# print( df.hist() )
