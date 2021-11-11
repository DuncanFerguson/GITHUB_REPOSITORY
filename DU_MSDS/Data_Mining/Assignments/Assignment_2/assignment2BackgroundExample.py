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

np.random.seed(0)

df = pd.read_csv("assignment2_cleanInfile.csv")
Y = df["RainTomorrow"].tolist()
df = df.drop(columns=["RainTomorrow"])
# print(Y)
# print(df)

x_train, x_test, y_train, y_test  = train_test_split(df, Y,  test_size=0.25, random_state=42)
# print('x_test = ' + str(x_test) )
# print('y_test = ' + str(y_test) )

#
#
print("\n\nDecision Tree:")
dtree = tree.DecisionTreeClassifier(criterion="gini")
dtree = dtree.fit(x_train,y_train)
y_predicted = dtree.predict(x_test)
print('DecisionTree confusion matrix:')
print(confusion_matrix( y_test, y_predicted))
importance = dtree.feature_importances_
accuracy = accuracy_score(y_test, y_predicted)
print('accuracy = ' + str(accuracy))
print("decision tree dtree feature importance:")
for i,v in enumerate(importance):
	print('Feature: %0d, FName: %15s, Score: %.5f' % (i,df.columns[i], v) )
	# print('Feature: %0d, Score: %.5f' % (i,v))
#
#
print("\n\nGausianNB:")
model = GaussianNB()
model.fit(x_train, y_train)
gausianNB_predicted = model.predict(x_test)
print('\nconfusion_matrix from Gaussian naive bayes:')
print(confusion_matrix( y_test, gausianNB_predicted ) )
accuracy = accuracy_score(y_test, gausianNB_predicted)
print('accuracy = ' + str(accuracy))
imps = permutation_importance(model, x_test, y_test)
print("gaussinaNB feature importance:")
print(imps.importances_mean)
#
#
#
# # now drop students attribute
# print("\n\nDropping student attribute")
# df2 = df.drop('student',axis=1)
# x_train, x_test, y_train, y_test  = train_test_split( df2, Y,  test_size=0.25, random_state=2)
# print(df2)
# print('x_test = ' + str(x_test) )
# print('y_test = ' + str(y_test) )
#
# print("\n\nDecision Tree:")
# dtree2 = tree.DecisionTreeClassifier(criterion="gini")
# dtree2 = dtree2.fit(x_train,y_train)
# y_predicted = dtree2.predict(x_test)
# print('DecisionTree confusion matrix:')
# print(confusion_matrix( y_test, y_predicted))
# importance = dtree2.feature_importances_
# print("decision tree dtree2 feature importance:")
# for i,v in enumerate(importance):
# 	print('Feature: %0d, FName: %15s, Score: %.5f' % (i,df2.columns[i], v) )
#
# print("\n\nGausianNB:")
# model2 = GaussianNB()
# model2.fit(x_train,y_train)
# gausianNB_predicted = model2.predict(x_test)
# print('\nconfusion_matrix from Gaussian naive bayes:')
# print(confusion_matrix( y_test, gausianNB_predicted ) )
# accuracy = accuracy_score(y_test, gausianNB_predicted)
# print('accuracy = ' + str(accuracy))
# imps = permutation_importance(model2, x_test, y_test)
# print("gaussinaNB feature importance:")
# print(imps.importances_mean)
