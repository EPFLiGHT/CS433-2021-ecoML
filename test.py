import numpy as np
import pandas as pd
import sklearn.linear_model
from sklearn.neural_network import MLPClassifier

from base import Cumulator
from country_dataset_helpers import dig3_to_dig2_conversion, drop_columns_keeping_max_year, dataset_converter
from sklearn.linear_model import LinearRegression
from sklearn import datasets
import sklearn

# Position
from implementations import add_dataset_row

dataset_converter('country_data.csv')

# Function

diabetes_X, diabetes_y = datasets.load_iris(return_X_y=True)

cumulator = Cumulator(hardware="gpu")
model = MLPClassifier(max_iter=2000, hidden_layer_sizes=(8, 8, 8))
cumulator.run(model.fit, X=diabetes_X, y=diabetes_y)
y = cumulator.run(model.predict, diabetes_X)
# print(y)
cumulator.display_carbon_footprint()

dataset = np.column_stack([diabetes_X, diabetes_y])
dataset = pd.DataFrame(dataset)
add_dataset_row(dataset, 0.1, 0.5, "NN", "Numeral")
