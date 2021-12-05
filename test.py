import sklearn.linear_model

from base import Cumulator
from country_dataset_helpers import dig3_to_dig2_conversion, drop_columns_keeping_max_year
from sklearn.linear_model import LinearRegression
from sklearn import datasets
import sklearn

# Position

a = Cumulator(hardware="gpu")
a.set_hardware("cpu")
a.position_carbon_intensity()
a = dig3_to_dig2_conversion("country_data.csv")
drop_columns_keeping_max_year(a)

# Function

diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

cumulator = Cumulator()
model = LinearRegression()
cumulator.run(model.fit, X=diabetes_X, y=diabetes_y)
y = cumulator.run(model.predict, diabetes_X)
print(y)
cumulator.display_carbon_footprint()
