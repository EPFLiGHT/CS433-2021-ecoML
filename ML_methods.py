from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import numpy as np


def random_forest(X_train, y_train, X_test, y_test):
    print('----------------RANDOM FOREST---------------')
    clf = RandomForestClassifier(max_depth=2, random_state=0)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(f'accuracy: {round(accuracy(y_pred, y_test), 2)}')


def logistic_regression(X_train, y_train, X_test, y_test):
    print('----------------LOGISTIC REGRESSION---------------')
    clf = LogisticRegression(random_state=0, max_iter=500)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(f'accuracy: {round(accuracy(y_pred, y_test), 2)}')


def linear_regression(X_train, y_train, X_test, y_test):
    print('----------------LINEAR REGRESSION---------------')
    clf = LinearRegression()
    reg = clf.fit(X_train, y_train)
    # print(f'score:{reg.score(X, y)}') #must check what it is to understand on which data to value
    print(f'coefficient:{reg.coef_}')
    print(f'intercept:{reg.intercept_}')
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(f'accuracy: {round(accuracy(y_pred, y_test), 2)}')


def accuracy(y_pred, y):
    return (np.power(y_pred - y, 2)).mean()
