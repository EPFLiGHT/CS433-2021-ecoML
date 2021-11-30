'''
This is the base class of cumulator.
'''
import json
import time as t
import geocoder
import random
import pandas as pd
from geopy.geocoders import Nominatim
import GPUtil

country_dataset_path = 'country_dataset_adjusted.csv'
gpu_dataset_path = 'hardware\gpu.csv'
metrics_dataset_path = 'metrics\CO2_metrics.csv'

class Cumulator:

    def __init__(self):
        default_TDP=250
        try:
            gpus = GPUtil.getGPUs()
            gpu_name=gpus[0].name
            df=pd.read_csv(gpu_dataset_path)
            #it uses contains for more flexibility
            row=df[df['name'].str.contains(gpu_name)]
            if row.empty:
                #if gpu not found then assign standard TDP
                TDP=default_TDP
            else:
                #otherwise assign gpu's TDP
                TDP=row.TDP.values[0]
        except:
            #in case no GPU can be found
            TDP=default_TDP
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
        self.hardware_load = TDP / 3.6e6
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
        #loading metrics dataset
        with open(metrics_dataset_path) as file:
            metrics=json.load(file)
            final_metrics=[]
            #computing equivalent of gCO2eq
            for metric in metrics:
                metric['equivalent']=metric['eq_factor']*(self.total_carbon_footprint())
                #keep only significative equivalent metrics
                if metrics['equivalent'] > 0:
                    final_metrics.appen(metric)
            l=len(final_metrics)
            if l>0:
                #select random equivalent metrics and print
                metric=final_metrics[random.randint(0,l-1)]
                print('\nThis carbon footprint is equivalent to {:2e} {}'.format(metric['equivalent'], metric['measure']))
        
