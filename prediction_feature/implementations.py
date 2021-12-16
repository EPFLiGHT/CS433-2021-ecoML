from sklearn.neural_network import MLPClassifier, MLPRegressor
import pandas as pd
# from base_repository.base import Cumulator
import torch
import torch.nn.functional as F
from torch import nn
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np
import os

rootdir = os.path.dirname(__file__)

from nn_utils import train

ROUND_ACCURACY = 4


def standard_neural_network(x_training_set, y_training_set, x_test_set, y_test_set, classification=True,
                            hidden_layer_size=(8, 8, 8), activation='relu', solver='adam', print_report=True):
    cumulator = Cumulator()
    if classification:
        alg = MLPClassifier(hidden_layer_size, activation=activation, solver=solver)
    else:
        alg = MLPRegressor(hidden_layer_size, activation=activation, solver=solver)

    cumulator.run(alg.fit, X=x_training_set, y=y_training_set)

    accuracy = alg.score(x_test_set, y_test_set)
    y_pred = alg.predict(x_test_set)

    if print_report:
        print(classification_report(y_test_set, y_pred))
    return round(accuracy, ROUND_ACCURACY), cumulator.return_total_carbon_footprint()


class LeNetModel(nn.Module):
    def __init__(self, activation_function: torch.nn.functional = torch.nn.functional.relu):
        """From: LeCun et al., 1998. Gradient-Based Learning Applied to Document Recognition"""
        super().__init__()
        self.activation_function = activation_function
        self.conv1 = torch.nn.Conv2d(1, 6, kernel_size=5)
        self.conv2 = torch.nn.Conv2d(6, 16, kernel_size=5)
        self.conv2_drop = torch.nn.Dropout2d()
        self.fc1 = torch.nn.Linear(256, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        max_pool2d = torch.nn.functional.max_pool2d

        x = self.activation_function(max_pool2d(self.conv1(x), 2))
        x = self.activation_function(max_pool2d(self.conv2(x), 2))
        x = torch.flatten(x, 1)
        x = self.activation_function(self.fc1(x))
        x = self.activation_function(self.fc2(x))
        x = self.fc3(x)
        return x


def lenet_neural_network(dataset_train, dataset_test, num_epochs=10, learning_rate=1e-3, print_report=True):
    cumulator = Cumulator()
    lenet_model = LeNetModel()

    # Loss and optimizer
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(lenet_model.parameters(), lr=learning_rate)

    # Training
    accuracy = cumulator.run(train, lenet_model, criterion, dataset_train, dataset_test, optimizer, num_epochs)
    # y_pred = alg.predict(x_test_set)

    # if print_report:
    # print(classification_report(y_test, y_pred))
    return round(accuracy, ROUND_ACCURACY), cumulator.return_total_carbon_footprint()


def random_forest(X_train, X_test, y_train, y_test, n_trees=100, max_depth=None, print_report=True):
    cumulator = Cumulator()
    print('----------------RANDOM FOREST---------------')
    clf = RandomForestClassifier(n_estimators=n_trees, max_depth=max_depth, random_state=0)
    cumulator.run(clf.fit, X=X_train, y=y_train)
    accuracy = clf.score(X_test, y_test)

    y_pred = clf.predict(X_test)

    if print_report:
        print(classification_report(y_test, y_pred))

    return round(accuracy, ROUND_ACCURACY), cumulator.return_total_carbon_footprint()


def logistic_regression(X_train, X_test, y_train, y_test, print_report=True):
    cumulator = Cumulator()
    print('----------------LOGISTIC REGRESSION---------------')
    clf = LogisticRegression(random_state=0, max_iter=500)
    cumulator.run(clf.fit, X=X_train, y=y_train)
    y_pred = clf.predict(X_test)
    # y_pred_rounded = rounder(y_train)(y_pred)
    y_pred_rounded = np.round(abs(y_pred))
    accuracy = accuracy_score(y_test, y_pred_rounded, normalize=True)

    if print_report:
        print(classification_report(y_test, y_pred_rounded))

    return round(accuracy, ROUND_ACCURACY), cumulator.return_total_carbon_footprint()


def linear_regression(X_train, X_test, y_train, y_test, print_report=True):
    cumulator = Cumulator()
    print('----------------LINEAR REGRESSION---------------')
    clf = LinearRegression()
    cumulator.run(clf.fit, X=X_train, y=y_train)
    y_pred = clf.predict(X_test)
    # y_pred_rounded = rounder(y_train)(y_pred)
    y_pred_rounded = np.round(abs(y_pred))
    accuracy = accuracy_score(y_test, y_pred_rounded, normalize=True)

    if print_report:
        print(classification_report(y_test, y_pred_rounded))

    return round(accuracy, ROUND_ACCURACY), cumulator.return_total_carbon_footprint()


# use rounder(y_train)(y_pred_to_round)
def rounder(y_train):
    values = np.array(list(set(y_train)))

    def f(x):
        idx = np.argmin(np.abs(values - x))
        return values[idx]

    return np.frompyfunc(f, 1, 1)
