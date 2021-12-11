from sklearn.neural_network import MLPClassifier, MLPRegressor
import pandas as pd
from base import Cumulator
import torch
import torch.nn.functional as F
from torch import nn

def add_dataset_row(dataset, accuracy, consumption, used_algorithm, type_of_dataset='None'):
    points, features = dataset.shape

    # MAX mutual Information between features and ML algorithm to use Computation
    # HERE
    #

    new_row = {'features': features, 'points': points, 'type': type_of_dataset, 'algo': used_algorithm, 'max_mut': 7,
               'accuracy': accuracy, 'consumption': consumption}

    # open dataset
    row = pd.DataFrame(new_row, index=[0])
    row.to_csv('ml_dataset.csv', mode='a', header=False)


def standard_neural_network(x_training_set, y_training_set, x_test_set, y_test_set, classification=True,
                            hidden_layer_size=(8, 8, 8), activation='relu', solver='adam'):
    cumulator = Cumulator()
    if classification:
        alg = MLPClassifier(hidden_layer_size, activation=activation, solver=solver)
    else:
        alg = MLPRegressor(hidden_layer_size, activation=activation, solver=solver)

    cumulator.run(alg.fit, X=x_training_set, y=y_training_set)

    accuracy = alg.score(x_test_set, y_test_set)

    print("accuracy is: " + str(accuracy))
    cumulator.display_carbon_footprint()


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