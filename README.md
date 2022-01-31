# CUMULATOR
A tool to quantify and report the carbon footprint of machine learning computations and communication in academia and healthcare

## Aim
Raise awareness about the carbon footprint of machine learning methods and to encourage further optimization and the rationale use of AI-powered tools. This work advocates for sustainable AI and the rational use of IT systems.
## Prerequisites
The tool works with Linux, Windows and MacOS
### Required Libraries
- [geocoder](https://geocoder.readthedocs.io)
- [geopy](https://geopy.readthedocs.io/en/stable/)
- [GPUtil](https://pypi.org/project/GPUtil/)
- [cpuinfo](https://pypi.org/project/py-cpuinfo/)

## Install and use
Free software: MIT license

To install CUMULATOR:
```
pip install cumulator
```
To import the script
```
from cumulator import base
```
To create a Cumulator instance
```
cumulator = base.Cumulator()
```

###Measure cost of computations
- First option: Activate or deactivate chronometer by using `cumulator.on()`, `cumulator.off()` whenever you perform ML computations (typically within each interation). It will automatically record each time duration in `cumulator.time_list` and sum it in `cumulator.cumulated_time()`. Then return carbon footprint due to all computations using `cumulator.computation_costs()`.
- Second option: Automatically track the cost of computation of a generic function with `cumulator.run(function, *args, **kwargs)` and then use `cumulator.computation_costs()` as before. An example is reported below:

```
cumulator = Cumulator()
model = LinearRegression()
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# without output and with keywords arguments
cumulator.run(model.fit, X=diabetes_X, y=diabetes_y)

# with output and without keywords arguments
y = cumulator.run(model.predict, diabetes_X)

# show results
cumulator.computation_costs()
```
###Measure cost of communications
Each time your models sends a data file to another node of the network, record the size of the file which is communicated (in kilo bytes) using `cumulator.data_transferred(file_size)`. The amount of data transferred is automatically recorded in c`umulator.file_size_list` and accumulated in `cumulator.cumulated_data_traffic`. Then return carbon footprint due to all communications using `cumulator.communication_costs()`.

###Display your total carbon footprint
Display the carbon footprint of your recorded actions with `cumulator.display_carbon_footprint()`:
```
########
Overall carbon footprint: 1.02e-08 gCO2eq
########
Carbon footprint due to computations: 1.02e-08 gCO2eq
Carbon footprint due to communications: 0.00e+00 gCO2eq
This carbon footprint is equivalent to 1.68e-13 incandescent lamps switched to leds.
```

## General info

This repository holds the implementation of the work done to improve Cumulator.

In the folder base_repository/ we improved the estimation of the consumption by adding the possibility to take into account the position of the user and the hardware used for the computations.
Then, we added a function so that the user does not have to start and stop Cumulator by hand, in order to make its use as comfortable as possible.
In addition, we integrated a continuous integration system to it (namely, Cirrus CI), in order to ease the approval of further improvements to Cumulator. 
Finally, we added new types of measures of consumption to give a better idea of the cost of computations in an everyday-life context.

In the folder prediction_feature/ we describe a new ambitious feature we integrated in Cumulator: a tool to lead the user to a green choice of which Machine Learning algorithm to use. Precisely, given a dataset, our tool will predict the F1 score and the consumption of different classification methods on this dataset, so that the user can choose the model that can reach an optimal trade off between utility and consumption.
\In order to realize this tool, we required what we call a meta-dataset, a dataset where rows represent datasets themselves, along with information about their training. As the authors are not aware of the existence of such a dataset, we designed a completely automated system to populate this meta-dataset: all the datasets are gathered from OpenML\cite{OpenML2013}, an online machine learning platform for sharing and organizing data, machine learning algorithms and experiments. Then, all the datasets will be trained with an AutoML tool. This will let us have an arbitrarily big meta-dataset, without the weight of training every single dataset by ourselves.
Beyond the scope of this work, we also believe this pipeline can be easily adopted for further ML tasks that require the training of a similar meta-dataset.

The team is composed by:

* Stefan Igescu (@nefagi-01)
* Giovanni Monea (@giommok)
* Vincenzo Pecorella (@vincenzopecorella)

## Libraries used
To improve the accuracy of the carbon footprint returned by cumulator we used CPUInfo, GPUutils, geocoder. The use of these libraries can also be avoided and Cumulator will use the standard parameters to estimate the consumption.
For visualization purposes and to handle the datasets we used matplotlib, sklearn, and pandas, but they are not required to run the models and the final training.


## Folders and Files

- `src`: contains all the .py files including all the helper functions used to prepare, elaborate and split the dataset. 
This folder also holds the implementations.py file with the ML methods used for regression.
- `notebooks`: contains a jupyter notebook that was used to explore the data and a project1.ipynb notebook with the full
pipeline with all the stages of feature engineering, model training and generating predictions.
- `report`: holds the project1_report.pdf with all the details of the implementation and the achieved results.

## Project structure
The project has been structured in the following way:
```markdown
├── README.md: this file.
├── .gitignore
├── .cirrus.yml
├── base_repository
│   ├──hardware
│   |   ├──cpu.csv: dataset with information about CPUs (including the TDP metric important for computing consumption)
│   |   ├──gpu.csv: dataset with information about GPUs (including the TDP metric important for computing consumption)
│   |   └──webscraper.py.csv: webscraper program used for obtaining the cpu.csv and gpu.csv from https://www.techpowerup.com/cpu-specs/ and https://www.techpowerup.com/gpu-specs/
│   ├──metrics
│   |   └──CO2_metrics.json: different metrics to express the carbon-footprint obtained from https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator
│   ├──countries
|   │   ├──contr_2_dig.json: helper to map 2-digit country code to 3-digit country code, used by country_dataset_helpers.py
|   │   ├──country_dataset_adjusted.csv: final country dataset exported by country_dataset_helpers.py and used by Cumulator
|   │   ├──test_cumulator.py: file for testing the feature predicting F1-score and consumption of different algorithm given a dataset
|   │   └──country_dataset_helpers.py: automatic script to transform the raw country dataset into the version used by Cumulator
│   ├──base.py: file containing definition of the Cumulator class implementing the tool
│   └──bonus.py: Cumulator original file, left unchanged
├── prediction_feature
|   ├── models: directory containing the saved trained models (4 models for F1, 4 models for consumption, thus 2 models per algorithm) and the respective RMSE (1 RMSE file for F1, 1 RMSE file for consumption)
|   ├── notebooks: directory with analysis and training on simple datasets done in different notebooks
|   ├── plots: directory containing the plots with the RMSE scores of the trained models (4 plots for F1, 4 plots for consumption)
|   ├── implementations.py: file containing the functions for training the model
|   ├── ml_dataset.csv: meta-dataset 
|   ├── mljar.py: file containing functions for AutoML and for generating the meta-dataset
|   ├── nn_utils.py: helper file for neural networks
|   ├── openml_datasets_retrieval.ipynb: notebook containing the procedure to populate the meta-dataset
|   ├── prediction_helper.py: helper file containing the function for computing the predictions
|   ├── regression.ipynb: notebook containing the procedure for training the models on the meta-dataset for predicting F1-score and consumption on a given dataset.
|   └── visualization_helpers.py: helper file containing the function for visualizing the predictions
└── tests
    └── test_base.py: unit tests for Cirrus
```

## Running the code

To automatically keep track of the consumption a generic function the method run() in base_repository/base.py can be used. An example of its use is reported below:
```

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
```
Future updates of the dataset of country consumption can be found on the [official page](https://github.com/owid/energy-data?country=). It needs to be slightly modified to be used by Cumulator. An automatic script to transform the dataset is given in base_repository/country_dataset_helpers.py
To update the hardware dataset instead, a script in base_repository/hardware/webscraper.py can be used.
For the other functionalities of cumulator please refer to the original repo of [Cumulator](https://github.com/epfl-iglobalhealth/cumulator).

To run the pipeline from the datasets fetching phase to the MLJar training phase a pre-made script can be found in prediction_feature/openml_datasets_retrieval.ipynb

The models to predict the F1 score and the consumption of a dataset in input with a specific ML algorithm can be found in prediction\models folder.

### Badges
[![Build Status](https://api.cirrus-ci.com/github/epfl-iglobalhealth/cumulator.svg)](https://cirrus-ci.com/github/epfl-iglobalhealth/cumulator)

