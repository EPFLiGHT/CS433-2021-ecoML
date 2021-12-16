import pandas as pd
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML
import os
import pandas as pd
from implementations import add_dataset_row
from sklearn.preprocessing import LabelEncoder
import numpy as np

rootdir = os.path.dirname(__file__)
results_dir = rootdir + '/results/'
dataset_dir = rootdir + '/datasets/'

algorithm_list = ['Linear', 'Random Forest', 'Decision Tree', 'Neural Network']


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
    for file_csv in os.listdir(dataset_dir):
        df = pd.read_csv(dataset_dir + file_csv, sep='[,;]')
        X_train, X_test, y_train, y_test = train_test_split(df[df.columns[:-1]], df[df.columns[-1]], test_size=0.25)
        automl = AutoML(algorithms=algorithm_list, eval_metric='f1', results_path=results_dir + file_csv.split('.')[0],
                        explain_level=1, top_models_to_improve=4, random_state=2)
        automl.fit(X_train, y_train)
        predictions = automl.predict(X_test)


def create_dataset():
    for dir in os.listdir(results_dir):
        for subdir in os.listdir(results_dir + dir):
            df = pd.read_csv(results_dir + dir + '/leaderboard.csv')
            dataset = pd.read_csv(dataset_dir + dir + '.csv')
            max_corr = compute_max_corr(dataset)
            df.apply(lambda x: add_dataset_row(dataset, x['metric_value'], x['train_time'], x['model_type'], max_corr),
                     axis=1)


# run_automl()
create_dataset()
