# CS433-2021-ecoML

## General info

This repository holds the implementation of the work done to improve Cumulator.

In the folder base_repository/ we improved the estimation of the consumption by adding the possibility to take into account the position of the user and the hardware used for the computations.
Then, we added a function so that the user does not have to start and stop Cumulator by hand, in order to make its use as comfortable as possible.
In addition, we integrated a continuous integration system to it (namely, Cirrus CI), in order to ease the approval of further improvements to Cumulator. 
Finally, we added new types of measures of consumption to give a better idea of the cost of computations in an everyday-life context.

In the folder prediction_feature/ we describe a new ambitious feature we integrated in Cumulator: a tool to lead the user to a green choice of which Machine Learning algorithm to use. Precisely, given a dataset, our tool will predict the F1 score and the consumption of different classification methods on this dataset, so that the user can choose the model that can reach an optimal trade off between utility and consumption.
\In order to realize this tool, we required what we call a meta-dataset, a dataset where rows represent datasets themselves, along with information about their training. As the authors are not aware of the existence of such a dataset, we designed a completely automated system to populate this meta-dataset: all the datasets are gathered from OpenML\cite{OpenML2013}, an online machine learning platform for sharing and organizing data, machine learning algorithms and experiments. Then, all the datasets will be trained with an AutoML tool. This will let us have an arbitrarily big meta-dataset, without the weight of training every single dataset by ourselves.
Beyond the scope of this work, we also believe this pipeline can be easily adopted for further ML tasks that require the training of a similar meta-dataset.

The team  ML GVA is composed by:

* Giovanni Monea (@giommok)
* Vincenzo Pecorella (@vincenzopecorella)
* Stefan Igescu (@nefagi-01)

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
│   ├──hardware: 
│   |   ├──cpu.csv: 
│   |   ├──gpu.csv: 
│   |   └──webscraper.py.csv: 
│   ├──metrics: 
│   |   └──CO2_metrics.json: 
│   ├──base.py: 
│   ├──bonus.py: 
│   ├──contr_2_dig.json: 
│   ├──country_dataset_adjusted.csv: 
│   ├──test_cumulator.py:
│   └──country_dataset_helpers.py: 
├── prediction_feature
|   ├── models:
|   ├── notebooks: 
|   ├── plots: 
|   ├── implementations.py: 
|   ├── ml_dataset.csv: 
|   ├── mljar.py: 
|   ├── nn_utils.py:
|   ├── openml_datasets_retrieval.ipynb:
|   ├── prediction_helper.py: 
|   ├── regression.ipynb:
|   └── visualization_helpers.py:
└── tests
    └── test_base.py
```

## Running the code

### Badges

[![Build Status](https://api.cirrus-ci.com/github/epfl-iglobalhealth/CS433-2021-ecoML.svg)](https://cirrus-ci.com/github/epfl-iglobalhealth/CS433-2021-ecoML)

