import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.naive_bayes import *
# from sklearn.naive_bayes import GaussianNB
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.naive_bayes import MultinomialNB


# feature vector = age, education-level, minoritized, pro-choice, gender
# where education level (0, 1, 2, 3 where 1 == HS, 2 == some college, 3 == bachelors+)
# pro-choice vs pro-life (0 means not pro-choice, i.e pro-life, 1 means yes pro-choice)
# minoritized = 0 means not identify as member of minoritized population
# gender:  0 means identify female, 1 means male, 2 means neither


tuples = []

# atuple = (age,education,minoritized,prochoice,gender,candidate)

atuple = (20,2,0,0,1,0)   #19, some college, not member of minoritized pop, not pro-choice male, voting for 0
tuples.append(atuple)

atuple = (22,3,1,1,1,1)     # voting for 1
tuples.append(atuple)

atuple = (30,2,1,1,1,1)     # voting for 1
tuples.append(atuple)

atuple = (60,3,0,0,0,0)   
tuples.append(atuple)

atuple = (40,3,1,1,2,1)     # voting for 1
tuples.append(atuple)

atuple = (34,3,1,1,1,0)   
tuples.append(atuple)

atuple = (32,3,0,0,1,0)   
tuples.append(atuple)

atuple = (36,0,0,1,1,1)     # voting for 1
tuples.append(atuple)

atuple = (24,2,0,0,1,0)   
tuples.append(atuple)

atuple = (27,3,1,1,1,1)     # voting for 1
tuples.append(atuple)

atuple = (37,2,1,1,1,1)     # voting for 1
tuples.append(atuple)

atuple = (80,3,0,0,0,0)   
tuples.append(atuple)

atuple = (33,3,1,1,2,1)     # voting for 1
tuples.append(atuple)

atuple = (39,3,1,1,1,0)   
tuples.append(atuple)

atuple = (39,3,0,0,1,0)   
tuples.append(atuple)

atuple = (38,0,0,1,1,1)     # voting for 1
tuples.append(atuple)



df = pd.DataFrame(tuples,columns=['age','education','minoritized','prochoice','gender','candidate'])
print(df)

X = df[ ['age','education','minoritized','prochoice','gender'] ]
Y = df[ 'candidate']

x_train, x_test, y_train, y_test  = train_test_split( X, Y,  test_size=0.25, random_state=1)
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

result = clf.predict_proba(x_test)
print('predict_proba(x_test) = ')
print(result)
result = clf.predict(x_test)
print('predict(x_test) = ')
print(result)

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

result = model.predict_proba(x_test)
print('predict_proba(x_test) = ')
print(result)
result = model.predict(x_test)
print('predict(x_test) = ')
print(result)

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

print('x_test = ')
print(x_test)
print('y_test = ')
print(y_test)

result = model.predict_proba(x_test)
print('predict_proba(x_test) = ')
print(result)
result = model.predict(x_test)
print('predict(x_test) = ')
print(result)


# print( df.hist() )
