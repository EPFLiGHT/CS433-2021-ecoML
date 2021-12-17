import pandas as pd
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

rootdir = os.path.dirname(__file__)
results_dir = rootdir + '/results/'
dataset_dir = rootdir + '/datasets_list_final/'
datasets_to_add_dir = rootdir + '/datasets_list_toadd/'

algorithm_list = ['Linear', 'Random Forest', 'Decision Tree', 'Neural Network']


def add_dataset_row(dataset, F1, time, used_algorithm, max_corr, type_of_dataset='None'):
    path = rootdir + "/ml_dataset.csv"
    points, features = dataset.shape

    # MAX mutual Information between features and ML algorithm to use Computation
    # HERE
    #

    new_row = {'features': features, 'points': points, 'type': type_of_dataset, 'algo': used_algorithm, 'F1': F1,
               'time': time, 'TDP': 250, 'country': 'Switzerland', 'max_corr': max_corr}

    # open dataset
    row = pd.DataFrame(new_row, index=[0])
    df = pd.read_csv(path)
    df = pd.concat([df, row])
    df = df.reset_index(drop=True)
    df.to_csv(path, index=False)


def encode_y(y):
    le = LabelEncoder()
    le.fit(y)
    y_enc = le.transform(y)
    return y_enc


def compute_max_corr(df):
    y = encode_y(df[df.columns[-1]])
    y = pd.Series(y)
    corr = df[df.columns[:-1]].corrwith(y)
    return np.max(np.absolute(corr))


def run_automl():
    listdir = os.listdir(datasets_to_add_dir)
    for index, file_csv in enumerate(listdir):
        print('\n\n\n\n\n\n\n\n DATASET ' + file_csv + ': ' + str(index) + ' of ' + str(len(listdir)))
        df = pd.read_csv(datasets_to_add_dir + file_csv, sep='[,]', engine='python')
        X_train, X_test, y_train, y_test = train_test_split(df[df.columns[:-1]], df[df.columns[-1]], test_size=0.25)
        automl = AutoML(algorithms=algorithm_list, eval_metric='f1', results_path=results_dir + file_csv.split('.')[0],
                        explain_level=1, top_models_to_improve=4, random_state=2, optuna_verbose=False)
        automl.fit(X_train, y_train)
        predictions = automl.predict(X_test)


def create_dataset():
    for dir in os.listdir(results_dir):
        print(dir)
        df = pd.read_csv(results_dir + dir + '/leaderboard.csv')
        dataset = pd.read_csv(dataset_dir + dir + '.csv')
        max_corr = compute_max_corr(dataset)
        df.apply(lambda x: add_dataset_row(dataset, x['metric_value'], x['train_time'], x['model_type'], max_corr), axis=1)

def extend_dataset(): # To use this, put the datasets in the datasets_list_toadd directory. Then, they will be added and moved to the datasets_list_final directory
    files_to_add = os.listdir(datasets_to_add_dir)
    for file_to_add in files_to_add:
        dir = file_to_add[:-4]
        print("Adding dataset %s ... " % dir, end='')
        df = pd.read_csv(results_dir + dir + '/leaderboard.csv')
        dataset = pd.read_csv(datasets_to_add_dir + dir + '.csv')
        max_corr = compute_max_corr(dataset)
        df.apply(lambda x: add_dataset_row(dataset, x['metric_value'], x['train_time'], x['model_type'], max_corr), axis=1)
        os.rename(datasets_to_add_dir + dir + '.csv', dataset_dir + dir + '.csv') # Move the file
        print('successfully added!')


    if len(files_to_add) == 0:
        print("There are no files to add. Please, make sure you put your files in the correct directory (datasets_list_toadd)")


#run_automl()
extend_dataset()
