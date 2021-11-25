from base import Cumulator
from country_dataset_helpers import dig3_to_dig2_conversion, drop_columns_keeping_max_year

a = Cumulator()
a.position_carbon_intensity()
a = dig3_to_dig2_conversion("country_data.csv")
drop_columns_keeping_max_year(a)