# DAML: DATA ANALYTICS ML Workflow for Binary Classification of Rare Disease Cohorts

## Environment Set Up

Before running the DAML workflow, a python environment with the required packages needs to be set up.

## Usage

There are multiple options that the program can take as parameters to change the run:

Parameter List

| parameter | data type | default value | description  |
| ------------- | ------------- | ------------- |------------- |
| --sample | int | 1000 | Number of samples in the simulated dataset  | 
| --feature  | int | 200000 | Number of features in the simulated dataset | 
| --balance  | float  | 0.5 | The balance ratio that corresponds to the number of samples in each cohort. (Value should be in the range of 0-1, higher than .50 means more samples in the disease cohort and viceversa) |
| --spikes  | int | 10 | Number of spikes injected into the simulated datasaet | 
| --threshold | float | .70 | The threshold that determines when a prediction is valid (Value should be in the rage of 0-1) | 
| --iterations  | int | 5 | Number of times the pipeline will run | 
| --my_functions  | boolean | False | Uses in-house validation functions (for the confusion matrix, ROC curve plots, etc) instead of the functions provided by scikit learn | 
| --test_type  | int | 0 | Determines the type of testing: 0 - analysis of single simulated dataset, 1 - spike combination analysis, 2 - feature analysis, 3 - sample analysis, 4 - dataset inbalance analysis | 

To run the workflow with the default settings: 

```bash
python main.py
``` 
