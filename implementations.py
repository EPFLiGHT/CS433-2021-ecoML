from sklearn.neural_network import MLPClassifier, MLPRegressor
import pandas as pd
from base import Cumulator


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
