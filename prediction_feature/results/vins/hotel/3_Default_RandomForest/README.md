# Summary of 3_Default_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.9
- **min_samples_split**: 30
- **max_depth**: 4
- **eval_metric_name**: f1
- **explain_level**: 1

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
f1

## Training time

10.1 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.210297 | nan         |
| auc       | 0.965453 | nan         |
| f1        | 0.87873  |   0.493371  |
| accuracy  | 0.922854 |   0.493371  |
| precision | 0.99802  |   0.952305  |
| recall    | 1        |   0.0175605 |
| mcc       | 0.825231 |   0.493371  |


## Confusion matrix (at threshold=0.493371)
|                         |   Predicted as City Hotel |   Predicted as Resort Hotel |
|:------------------------|--------------------------:|----------------------------:|
| Labeled as City Hotel   |                     14402 |                         463 |
| Labeled as Resort Hotel |                      1264 |                        6257 |

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
