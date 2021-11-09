import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.naive_bayes import *
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn.inspection import permutation_importance
from itertools import combinations

def train_data(df, drops=None):
    """This function trains the data and returns the desired drops"""
    # Y is the classification
    Y = df['RainTomorrow'].tolist()

    X = df
    X = X.drop(columns=["RainTomorrow"])
    if drops != None:
        X = X.drop(columns=drops)

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=2)
    return x_train, x_test, y_train, y_test, X

def decisionTree_Model(x_train, x_test, y_train, y_test, X):
    """This Function Goes through and prints out the Decision tree model"""
    # Building out a decision tree
    dtree = tree.DecisionTreeClassifier(criterion="gini")
    dtree = dtree.fit(x_train, y_train)
    y_predicted = dtree.predict(x_test)
    accuracy = accuracy_score(y_test, y_predicted)
    important = dtree.feature_importances_
    df_importance_list = []
    for i, v in enumerate(important):
        df_importance_list.append([X.columns[i], v])
    df_importance = pd.DataFrame(df_importance_list, columns=["FName", "Score"])
    df_importance.sort_values(by=['Score'], ascending=False, inplace=True)
    decisionTree_Model_Features = df_importance["FName"].tolist()
    return accuracy, decisionTree_Model_Features

def GausianNB_Model(x_train, x_test, y_train, y_test, X):
    """This Function takes in the training and the testing models to help create the GausianNB Model"""
    model2 = GaussianNB()
    model2.fit(x_train, y_train)
    gausianNB_predicted = model2.predict(x_test)
    accuracy = accuracy_score(y_test, gausianNB_predicted)
    imps = permutation_importance(model2, x_test, y_test)
    df_Gausian_Feature_Importance_List = []
    Gausian_Feature_Importance_List = imps.importances_mean.tolist()
    for row in enumerate(Gausian_Feature_Importance_List):
        df_Gausian_Feature_Importance_List.append([X.columns[row[0]], row[1]])
    df_Gausian_Feature_Importance = pd.DataFrame(df_Gausian_Feature_Importance_List, columns=["Feature", "Significance"])
    df_Gausian_Feature_Importance.sort_values(by=["Significance"], ascending=False, inplace=True)
    GausianND_Features = df_Gausian_Feature_Importance["Feature"].tolist()
    return accuracy, GausianND_Features

def forward_selection():
    """This Function goes through and use's forward selection"""



def main():
    np.random.seed(0)
    df = pd.read_csv("assignment2_cleanInfile.csv")
    features = df.columns.tolist()
    features.pop(-1)
    # all_combinations = list(combinations(features, i))

    for i in range(1, len(features)):
        print(features[::-i])
        # print(i)
    #     all_combinations = list(combinations(features, i))
    #     for combo in all_combinations:
    #         combo = list(combo)
    #         x_train, x_test, y_train, y_test, X = train_data(df, combo)
    #         accuracy, features = decisionTree_Model(x_train, x_test, y_train, y_test, X)
    #         if accuracy >= best_accuracy:
    #             best_accuracy = accuracy
    #             best_features = features
    #
    # print(best_accuracy, best_features)



if __name__ == '__main__':
    main()
