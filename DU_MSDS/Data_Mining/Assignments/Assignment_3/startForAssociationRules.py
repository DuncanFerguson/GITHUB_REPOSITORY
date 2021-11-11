# This program assume the input.csv data set is the bank data set found in:
# It assume the data set is the bank direct marking data set found in: 
#       https://www.kaggle.com/psvishnu/bank-direct-marketing
# This program reads in 'input.csv' into a dataframe and then cleans it to prepare for association rules as follows:
# a) leaves things as strings, NOT numerical data
# b) converts numerical data into strings.  For example, balance converted to one of "very negative, negative, positive, very positive".  Similar for age
# c) changes yes/no for housing, default, and loan into:  housingYes/housingNo etc (so they are distinguishable from the other columns)

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


df = df.drop('pdays',axis=1)

for index, row in df.iterrows():
	if row['balance'] < 0:
		row['balance'] = 'inDebt'
	else:
		row['balance'] = 'notInDebt'
	
df.loc[( df['balance'] >= 10000), 'balanceSummary'] = 'veryPositive' 
df.loc[( (df['balance'] < 0) & (df['balance'] >= -10000)), 'balanceSummary'] = 'negative' 
df.loc[( (df['balance'] < 10000) & (df['balance'] >= 0)), 'balanceSummary'] = 'positive' 
df.loc[df['balance'] < -500, 'balanceSummary'] = 'veryNegative' 


df.loc[( (df['age'] < 25) & (df['age'] >= 0)),  'ageBand'] = 'ageBand1' 
df.loc[( (df['age'] < 30) & (df['age'] >= 25)), 'ageBand'] = 'ageBand2' 
df.loc[( (df['age'] < 40) & (df['age'] >= 30)), 'ageBand'] = 'ageBand3' 
df.loc[( (df['age'] < 50) & (df['age'] >= 40)), 'ageBand'] = 'ageBand4' 
df.loc[( (df['age'] < 120) & (df['age'] >= 50)),'ageBand'] = 'ageBand5' 

df.loc[ (df['default'] == 'no'), 'defaultValue'] = 'defaultNo' 
df.loc[ (df['default'] == 'yes'), 'defaultValue'] = 'defaultYes' 
df.loc[ (df['housing'] == 'no'), 'housingVal'] = 'houseNo' 
df.loc[ (df['housing'] == 'yes'), 'housingVal'] = 'houseYes' 
df.loc[ (df['loan'] == 'no'), 'loanVal'] = 'loanNo' 
df.loc[ (df['loan'] == 'yes'), 'loanVal'] = 'loanYes' 



# df['balanceSummary'] = df['balance'].apply(lambda x: 'negative' if x <= 0 else 'positive')
# df['balanceSummary'] = df['balance'].apply(lambda x: 'negative' if x <= 0 else 'positive')

# print("df['balance'].max() = " + str( df['balance'].max() ))


# df['balance'] = (df['balance'] - df['balance'].min()) / ( df['balance'].max() - df['balance'].min() )
# df['balance'] = 100.0 * (df['balance'] - df['balance'].min()) / ( df['balance'].max() - df['balance'].min() )
print("\n\nAfter converting to numeric, dropping pdays, and normalizing balance:")
print( df.head(10) )


# now drop stuff that is not a string

# Y = df['y']
# df = df.drop('y',axis=1)   # do not drop yes/no so you can make then subset rules into those that show "yes" versus "no"
df = df.drop('age',axis=1)
df = df.drop('day',axis=1)
df = df.drop('duration',axis=1)
df = df.drop('balance',axis=1)
df = df.drop('campaign',axis=1)
df = df.drop('previous',axis=1)
df = df.drop('default',axis=1)
df = df.drop('housing',axis=1)
df = df.drop('loan',axis=1)

print("\n\nFinal df:")
print( df.head(100) )


df.to_csv('outfile.csv',index = False )
