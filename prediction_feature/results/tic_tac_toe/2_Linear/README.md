# Summary of 2_Linear

[<< Go back](../README.md)


## Logistic Regression (Linear)
- **n_jobs**: -1
- **explain_level**: 1

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
f1

## Training time

0.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.623729 |  nan        |
| auc       | 0.620133 |  nan        |
| f1        | 0.788732 |    0.474393 |
| accuracy  | 0.677778 |    0.534248 |
| precision | 1        |    0.803534 |
| recall    | 1        |    0.327377 |
| mcc       | 0.220567 |    0.534248 |


## Confusion matrix (at threshold=0.534248)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      18 |                      45 |
| Labeled as positive |                      13 |                     104 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                |   Learner_1 |
|:-----------------------|------------:|
| intercept              |   0.665397  |
| "middle-middle-square" |   0.292638  |
| "bottom-right-square"  |   0.15263   |
| "top-right-square"     |   0.134958  |
| "top-left-square"      |   0.0438993 |
| "bottom-left-square"   |   0.0297839 |
| "top-middle-square"    |  -0.13832   |
| "bottom-middle-square" |  -0.173165  |
| "middle-right-square"  |  -0.212714  |
| "middle-left-square"   |  -0.235445  |


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
