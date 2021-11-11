# This program assume the input.csv data set is the bank data set found in:
# It assume the data set is the bank direct marking data set found in: 
#       https://www.kaggle.com/psvishnu/bank-direct-marketing
# This program reads in 'input.csv' into a dataframe and then cleans it as follows:
# a) converts all string to categorical data; b) drops the column 'pdays'; 
# and c) normalizes the 'balance' column

import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.naive_bayes import *
# from sklearn.naive_bayes import GaussianNB
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.naive_bayes import MultinomialNB


pd.set_option('display.max_columns', None)
pd.set_option('max_columns', None)
pd.set_option('max_rows', None)
pd.options.display.width = 0   # automatically ajust to window length

df = pd.read_csv('input.csv')

print("\n\nOriginal data set:")
print( df.head() )


# change all non-numeric into category data
df['job'] = df['job'].astype('category')
df['job'] = df['job'].cat.codes
df['marital'] = df['marital'].astype('category')
df['marital'] = df['marital'].cat.codes
df['education'] = df['education'].astype('category')
df['education'] = df['education'].cat.codes
df['default'] = df['default'].astype('category')
df['default'] = df['default'].cat.codes
df['contact'] = df['contact'].astype('category')
df['contact'] = df['contact'].cat.codes
df['month'] = df['month'].astype('category')
df['month'] = df['month'].cat.codes
df['poutcome'] = df['poutcome'].astype('category')
df['poutcome'] = df['poutcome'].cat.codes
df['housing'] = df['housing'].astype('category')
df['housing'] = df['housing'].cat.codes
df['loan'] = df['loan'].astype('category')
df['loan'] = df['loan'].cat.codes
df['y'] = df['y'].astype('category')
df['y'] = df['y'].cat.codes

df = df.drop('pdays',axis=1)


df['balance'] = (df['balance'] - df['balance'].min()) / ( df['balance'].max() - df['balance'].min() )
print("\n\nAfter converting to numeric, dropping pdays, and normalizing balance:")
print( df.head(100) )



# now create X and Y for machine learning algoirthms

Y = df['y']
df = df.drop('y',axis=1)
X = df


# partition into training and testing sets
x_train, x_test, y_train, y_test  = train_test_split( X, Y,  test_size=0.20, random_state=1)
print('len(x_train), len(y_train) = ' + str(len(x_train)) + ',' + str(len(y_train)) )
print('len(x_test), len(y_test) = ' + str(len(x_test)) + ',' + str(len(y_test)) )


# run decision tree
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


# run GaussianNB
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

