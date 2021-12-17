# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                   |   Weight |
|:------------------------|---------:|
| 2_Default_NeuralNetwork |        1 |

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.323541 | nan           |
| auc       | 0.90587  | nan           |
| f1        | 0.687577 |   0.342664    |
| accuracy  | 0.851824 |   0.450195    |
| precision | 0.980822 |   0.978502    |
| recall    | 1        |   3.49125e-08 |
| mcc       | 0.580482 |   0.342664    |


## Confusion matrix (at threshold=0.450195)
|                   |   Predicted as  <=50K |   Predicted as  >50K |
|:------------------|----------------------:|---------------------:|
| Labeled as  <=50K |                  6468 |                  484 |
| Labeled as  >50K  |                   873 |                 1333 |

## Learning curves
![Learning curves](learning_curves.png)
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
