'''
This is the base class of cumulator.
'''
import json
import time as t
import geocoder
import pandas as pd
from geopy.geocoders import Nominatim

country_dataset_path = 'country_dataset_adjusted.csv'


class Cumulator:

    def __init__(self):
        self.t0 = 0
        self.t1 = 0
        # times are in seconds
        self.time_list = []
        self.cumulated_time = 0
        # file sizes are in bytes
        self.file_size_list = []
        self.cumulated_data_traffic = 0
        # number of GPU
        self.n_gpu = 1
        # assumptions to approximate the carbon footprint
        # computation costs: consumption of a typical GPU in Watts converted to kWh/s
        self.hardware_load = 250 / 3.6e6
        # communication costs: average energy impact of traffic in a typical data centers, kWh/kB
        self.one_byte_model = 6.894E-8
        # conversion to carbon footprint: average carbon intensity value in gCO2eq/kWh in the EU in 2014
        self.carbon_intensity = 447

    # starts accumulating time
    def on(self):
        self.t0 = t.time()

    # stops accumulating time and records the value
    def off(self):
        self.t1 = t.time()
        self.cumulated_time += self.t1 - self.t0
        self.time_list.append(self.t1 - self.t0)

    def run(self, function, *args, **kwargs):
        """
        Measure the carbon footprint of `function`.

        Example
        --------
        >>> # imports
        >>> from sklearn.linear_model import LinearRegression
        >>> from sklearn import datasets
        >>> # initialization
        >>> cumulator = Cumulator()
        >>> model = LinearRegression()
        >>> diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
        >>> # without output and with keywords arguments
        >>> cumulator.run(model.fit, X=diabetes_X, y=diabetes_y)
        >>> # with output and without keywords arguments
        >>> y = cumulator.run(model.predict, diabetes_X)
        >>> # show results
        >>> cumulator.display_carbon_footprint()


        :param function: function to measure.
        :param args: positional arguments of `function`.
        :param kwargs: keywords arguments of `function`.
        :return: output of `function`.
        """
        self.on()
        output = function(*args, **kwargs)
        self.off()
        return output

    def position_carbon_intensity(self):
        geolocator = Nominatim(user_agent="cumulator")
        g = geocoder.ip('me')
        df_data = pd.read_csv(country_dataset_path)

        location = geolocator.reverse(g.latlng)
        address = location.raw['address']
        code = address.get('country_code').upper()
        df_row = df_data[df_data['country'] == code]
        self.carbon_intensity = float(df_row['co2_per_unit_energy']*1000 if not df_row.empty else self.carbon_intensity)
        print(self.carbon_intensity)

    # records the amount of data transferred, file_size in kilo bytes
    def data_transferred(self, file_size):
        self.file_size_list.append(file_size)
        self.cumulated_data_traffic += file_size

    # computes time based carbon footprint due to computations
    def computation_costs(self):
        return self.cumulated_time * self.n_gpu * self.hardware_load * self.carbon_intensity

    # computes the carbon footprint due to communication
    def communication_costs(self):
        return self.one_byte_model * self.cumulated_data_traffic * self.carbon_intensity

    # computes the total carbon footprint
    def total_carbon_footprint(self):
        return self.computation_costs() + self.communication_costs()

    # prints the carbon footprint in the terminal
    def display_carbon_footprint(self):
        print('########\nOverall carbon footprint: %s gCO2eq\n########' %
              "{:.2e}".format(self.total_carbon_footprint()))
        print('Carbon footprint due to computations: %s gCO2eq' %
              "{:.2e}".format(self.computation_costs()))
        print('Carbon footprint due to communications: %s gCO2eq' %
              "{:.2e}".format(self.communication_costs()))
