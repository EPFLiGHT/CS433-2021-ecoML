# Summary of 1_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: entropy
- **max_depth**: 4
- **explain_level**: 1

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
f1

## Training time

16.0 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.213691 | nan          |
| auc       | 0.957992 | nan          |
| f1        | 0.869498 |   0.500181   |
| accuracy  | 0.917091 |   0.500181   |
| precision | 0.998318 |   0.965867   |
| recall    | 1        |   0.00195331 |
| mcc       | 0.811935 |   0.500181   |


## Confusion matrix (at threshold=0.500181)
|                         |   Predicted as City Hotel |   Predicted as Resort Hotel |
|:------------------------|--------------------------:|----------------------------:|
| Labeled as City Hotel   |                     14347 |                         518 |
| Labeled as Resort Hotel |                      1338 |                        6183 |

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


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



[<< Go back](../README.md)