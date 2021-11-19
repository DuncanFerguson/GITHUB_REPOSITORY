import numpy as np
import math
import pandas as pd
from sklearn import tree
from sklearn.naive_bayes import *
from sklearn.metrics import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.inspection import permutation_importance
from sklearn.decomposition import PCA


def runGaussianNB():
	global gausianNB_predicted
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


df = pd.read_csv('cleanInfile.csv')
print(df)

Y = df['RainTomorrow']
print(Y)

df = df.drop('RainTomorrow',axis=1)
print(df.head())
x_train, x_test, y_train, y_test  = train_test_split( df, Y,  test_size=0.20, random_state=1)
save_xtrain = x_train
save_xtest = x_test
save_ytrain = y_train
save_ytest = y_test
# runDecisionTree()
runGaussianNB()


print("\n\n")
pca = PCA()
x_train = pca.fit_transform(save_xtrain)
x_test = pca.fit_transform(save_xtest)
explained_variance = pca.explained_variance_ratio_
print("explained_variance = ")
print(explained_variance)


print("\n\nRun with ALL components")
x_train = save_xtrain
x_test = save_xtest
runGaussianNB()
accuracyAll = accuracy_score(y_test, gausianNB_predicted)


#  now run with 1 component
print("\n\nRun with number of components = 1")
pca = PCA(n_components=1)
x_train = pca.fit_transform(save_xtrain)
x_test = pca.fit_transform(save_xtest)
runGaussianNB()
accuracy1 = accuracy_score(y_test, gausianNB_predicted)


# print out the accuracies from above in a table
print("\n\nAccuracies:")
print("all - " + str(accuracyAll))
print("  1 - " + str(accuracy1))


