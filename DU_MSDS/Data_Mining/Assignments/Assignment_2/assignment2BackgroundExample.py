#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.naive_bayes import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.inspection import permutation_importance



# Data and classifications here from Table 8.1 of the 3rd edition of Han, Kamber and Pei book



# t1 =  ['youth','high','no','fair']  # would map to:     [0, 2, 0, 0 ]
# age: youth = 0, middle = 1, senior = 2
# income: low = 0, medium = 1, hight = 2
# student: no = 0, yes = 1
# credit: fair = 0, good = 1, excellent = 2  


# end of line number is specified classification of 0 or 1
nt1 =  [0,2,0,0]  # 0
nt2 =  [0,2,0,2]  # 0
nt3 =  [1,2,0,0]  # 0
nt4 =  [2,1,0,2]  # 0
nt5 =  [2,0,1,0]  # 1
nt6 =  [2,0,1,2]  # 1
nt7 =  [1,0,1,0]  # 1
nt8 =  [0,1,0,0]  # 0
nt9 =  [0,0,1,2]  # 1
nt10 = [2,1,1,0]  # 1

nt11 = [0,1,1,0]  # 1
nt12 = [1,1,0,2]  # 0
nt13 = [1,2,1,2]  # 1
nt14 = [2,1,1,0]  # 0
nt15 = [0,1,1,2]  # 1
nt16 = [0,1,1,0]  # 1
nt17 = [0,0,1,2]  # 1
nt18 = [2,1,0,2]  # 1
nt19 = [2,0,0,2]  # 0
nt20 = [2,1,0,0]  # 0

nt21 = [2,1,1,0]  # 1
nt22 = [2,1,1,0]  # 1
nt23 = [2,1,1,0]  # 1
nt24 = [2,1,0,0]  # 0


# classifications are:
Y = [0,0,0,0,1,1,1,0,1,1,  1,0,1,0,1,1,1,1,0,0,  1,1,1,0]

theData = []
theData.append(nt1)
theData.append(nt2)
theData.append(nt3)
theData.append(nt4)
theData.append(nt5)
theData.append(nt6)
theData.append(nt7)
theData.append(nt8)
theData.append(nt9)
theData.append(nt10)
theData.append(nt11)
theData.append(nt12)
theData.append(nt13)
theData.append(nt14)
theData.append(nt15)
theData.append(nt16)
theData.append(nt17)
theData.append(nt18)
theData.append(nt19)
theData.append(nt20)
theData.append(nt21)
theData.append(nt22)
theData.append(nt23)
theData.append(nt24)

df = pd.DataFrame(theData)
df.columns = ['age','income','student','credit']
print(Y)
print(df)

x_train, x_test, y_train, y_test  = train_test_split( df, Y,  test_size=0.25, random_state=2)
print('x_test = ' + str(x_test) )
print('y_test = ' + str(y_test) )



print("\n\nDecision Tree:")
dtree = tree.DecisionTreeClassifier(criterion="gini")
dtree = dtree.fit(x_train,y_train)
y_predicted = dtree.predict(x_test)
print('DecisionTree confusion matrix:')
print(confusion_matrix( y_test, y_predicted))
importance = dtree.feature_importances_
print("decision tree dtree feature importance:")
for i,v in enumerate(importance):
	print('Feature: %0d, FName: %15s, Score: %.5f' % (i,df.columns[i], v) )
	# print('Feature: %0d, Score: %.5f' % (i,v))


print("\n\nGausianNB:")
model = GaussianNB()
model.fit(x_train,y_train)
gausianNB_predicted = model.predict(x_test)
print('\nconfusion_matrix from Gaussian naive bayes:')
print(confusion_matrix( y_test, gausianNB_predicted ) )
accuracy = accuracy_score(y_test, gausianNB_predicted)
print('accuracy = ' + str(accuracy))
imps = permutation_importance(model, x_test, y_test)
print("gaussinaNB feature importance:")
print(imps.importances_mean)



# now drop students attribute
print("\n\nDropping student attribute")
df2 = df.drop('student',axis=1)
x_train, x_test, y_train, y_test  = train_test_split( df2, Y,  test_size=0.25, random_state=2)
print(df2)
print('x_test = ' + str(x_test) )
print('y_test = ' + str(y_test) )

print("\n\nDecision Tree:")
dtree2 = tree.DecisionTreeClassifier(criterion="gini")
dtree2 = dtree2.fit(x_train,y_train)
y_predicted = dtree2.predict(x_test)
print('DecisionTree confusion matrix:')
print(confusion_matrix( y_test, y_predicted))
importance = dtree2.feature_importances_
print("decision tree dtree2 feature importance:")
for i,v in enumerate(importance):
	print('Feature: %0d, FName: %15s, Score: %.5f' % (i,df2.columns[i], v) )

print("\n\nGausianNB:")
model2 = GaussianNB()
model2.fit(x_train,y_train)
gausianNB_predicted = model2.predict(x_test)
print('\nconfusion_matrix from Gaussian naive bayes:')
print(confusion_matrix( y_test, gausianNB_predicted ) )
accuracy = accuracy_score(y_test, gausianNB_predicted)
print('accuracy = ' + str(accuracy))
imps = permutation_importance(model2, x_test, y_test)
print("gaussinaNB feature importance:")
print(imps.importances_mean)
