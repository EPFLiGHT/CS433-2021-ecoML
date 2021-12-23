from base import Cumulator
from sklearn.datasets import load_iris,load_diabetes
import pandas as pd
import numpy as np

a = Cumulator()
iris = load_diabetes()
data1 = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])

a.predict_consumptions_f1(data1, 'target')