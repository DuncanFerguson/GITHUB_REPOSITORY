import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.naive_bayes import *
# from sklearn.naive_bayes import GaussianNB
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.naive_bayes import MultinomialNB

# three clusters

np.random.seed(1)

def equalProb():  # returns 0 or 1 with equal probablity
	if (np.random.random() < 0.95):
		return(0)
	else:
		return(1)

def boundedNormal(bound,stddev):
	rNum = np.random.normal(0,stddev)
	while rNum < -bound or rNum > bound:
		rNum = np.random.normal(0,stddev)
	return(rNum)

center1 = 10
center2 = 15
center3 = 30
bound = 10
stddev = 2

tuples = []
numTuples = 1000

for i in range(numTuples):
	rNum = np.random.randint(3)
	if (rNum == 0):
		candidate = 0

		rNum = boundedNormal(bound+5, stddev)
		a1 = center1 + rNum + 6

		rNum = boundedNormal(bound+5, stddev)
		a2 = center1 + rNum


	elif (rNum == 1):
		candidate = 1

		rNum = boundedNormal(bound,stddev+5)
		a1 = center2 + rNum

		rNum = boundedNormal(bound,stddev+5)
		a2 = center2 + rNum

	
	else:
		candidate = 2

		rNum = boundedNormal(bound,stddev+2)
		a1 = center3 + rNum

		rNum = boundedNormal(bound,stddev+2)
		a2 = center3 + rNum

	atuple = (a1,a2)
	# atuple = (a1,a2,a3,candidate)
	tuples.append(atuple)





# df = pd.DataFrame(tuples,columns=['a1','a2','a3','candidate'])
df = pd.DataFrame(tuples,columns=['a1','a2'])
# print(df)

df.to_csv('outfile.csv', index=False)
# df.to_csv('outfile.csv')



