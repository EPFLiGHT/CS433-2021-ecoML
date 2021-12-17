# Summary of 1_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: entropy
- **max_depth**: 4
- **num_class**: 20
- **explain_level**: 1

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.9
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
f1

## Training time

15.8 seconds

### Metric details
|           |        1 |   2 |    3 |        4 |   5 |        6 |   7 |   8 |        9 |   10 |   11 |       12 |       13 |   14 |       15 |   16 |   17 |   18 |       19 |       20 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------:|----:|-----:|---------:|----:|---------:|----:|----:|---------:|-----:|-----:|---------:|---------:|-----:|---------:|-----:|-----:|-----:|---------:|---------:|-----------:|------------:|---------------:|----------:|
| precision | 1        | 0.5 | 0.75 | 1        |   0 | 0.153846 |   0 |   0 | 1        |    0 |    0 | 0.666667 | 0.5      |    0 | 1        |    1 |  0.6 |    0 | 0.333333 | 0.333333 |        0.5 |    0.441859 |       0.499466 |   2.35955 |
| recall    | 0.5      | 0.5 | 0.75 | 0.5      |   0 | 1        |   0 |   0 | 0.5      |    0 |    0 | 1        | 1        |    0 | 0.666667 |    1 |  0.6 |    0 | 1        | 0.5      |        0.5 |    0.475833 |       0.5      |   2.35955 |
| f1-score  | 0.666667 | 0.5 | 0.75 | 0.666667 |   0 | 0.266667 |   0 |   0 | 0.666667 |    0 |    0 | 0.8      | 0.666667 |    0 | 0.8      |    1 |  0.6 |    0 | 0.5      | 0.4      |        0.5 |    0.414167 |       0.458333 |   2.35955 |
| support   | 4        | 2   | 4    | 2        |   2 | 2        |   2 |   2 | 2        |    2 |    2 | 2        | 2        |    2 | 3        |    2 |  5   |    2 | 2        | 2        |        0.5 |   48        |      48        |   2.35955 |


## Confusion matrix
|               |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |   Predicted as 5 |   Predicted as 6 |   Predicted as 7 |   Predicted as 8 |   Predicted as 9 |   Predicted as 10 |   Predicted as 11 |   Predicted as 12 |   Predicted as 13 |   Predicted as 14 |   Predicted as 15 |   Predicted as 16 |   Predicted as 17 |   Predicted as 18 |   Predicted as 19 |   Predicted as 20 |
|:--------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|------------------:|
| Labeled as 1  |                2 |                0 |                0 |                0 |                0 |                1 |                0 |                0 |                0 |                 0 |                 0 |                 1 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |
| Labeled as 2  |                0 |                1 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 1 |
| Labeled as 3  |                0 |                0 |                3 |                0 |                0 |                1 |                0 |                0 |                0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |
| Labeled as 4  |                0 |                0 |                0 |                1 |                0 |                0 |                0 |                0 |                0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 1 |
| Labeled as 5  |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 2 |                 0 |
| Labeled as 6  |                0 |                0 |                0 |                0 |                0 |                2 |                0 |                0 |                0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |
| Labeled as 7  |                0 |                0 |                0 |                0 |                0 |                2 |                0 |                0 |                0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |
| Labeled as 8  |                0 |                0 |                0 |                0 |                0 |                2 |                0 |                0 |                0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |
| Labeled as 9  |                0 |                0 |                0 |                0 |                0 |                1 |                0 |                0 |                1 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |
| Labeled as 10 |                0 |                0 |                0 |                0 |                0 |                2 |                0 |                0 |                0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |
| Labeled as 11 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                 0 |                 0 |                 0 |                 2 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |
| Labeled as 12 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                 0 |                 0 |                 2 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |
| Labeled as 13 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                 0 |                 0 |                 0 |                 2 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |
| Labeled as 14 |                0 |                0 |                1 |                0 |                0 |                0 |                0 |                0 |                0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 1 |                 0 |                 0 |                 0 |
| Labeled as 15 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 2 |                 0 |                 1 |                 0 |                 0 |                 0 |
| Labeled as 16 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 2 |                 0 |                 0 |                 0 |                 0 |
| Labeled as 17 |                0 |                0 |                0 |                0 |                0 |                2 |                0 |                0 |                0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 3 |                 0 |                 0 |                 0 |
| Labeled as 18 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 2 |                 0 |
| Labeled as 19 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 2 |                 0 |
| Labeled as 20 |                0 |                1 |                0 |                0 |                0 |                0 |                0 |                0 |                0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 0 |                 1 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Precision Recall Curve

![Precision Recall Curve](precision_recall_curve.png)



[<< Go back](../README.md)
