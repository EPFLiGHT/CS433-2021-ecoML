# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model    |   Weight |
|:---------|---------:|
| 2_Linear |        1 |

### Metric details
|           |   Cyclic |   Decreasing_trend |   Downward_shift |   Increasing_trend |   Normal |   Upward_shift |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------:|-------------------:|-----------------:|-------------------:|---------:|---------------:|-----------:|------------:|---------------:|----------:|
| precision |        1 |                  1 |                1 |                  1 |        1 |              1 |          1 |           1 |              1 |  0.023658 |
| recall    |        1 |                  1 |                1 |                  1 |        1 |              1 |          1 |           1 |              1 |  0.023658 |
| f1-score  |        1 |                  1 |                1 |                  1 |        1 |              1 |          1 |           1 |              1 |  0.023658 |
| support   |       21 |                 17 |               19 |                 19 |       19 |             18 |          1 |         113 |            113 |  0.023658 |


## Confusion matrix
|                             |   Predicted as Cyclic |   Predicted as Decreasing_trend |   Predicted as Downward_shift |   Predicted as Increasing_trend |   Predicted as Normal |   Predicted as Upward_shift |
|:----------------------------|----------------------:|--------------------------------:|------------------------------:|--------------------------------:|----------------------:|----------------------------:|
| Labeled as Cyclic           |                    21 |                               0 |                             0 |                               0 |                     0 |                           0 |
| Labeled as Decreasing_trend |                     0 |                              17 |                             0 |                               0 |                     0 |                           0 |
| Labeled as Downward_shift   |                     0 |                               0 |                            19 |                               0 |                     0 |                           0 |
| Labeled as Increasing_trend |                     0 |                               0 |                             0 |                              19 |                     0 |                           0 |
| Labeled as Normal           |                     0 |                               0 |                             0 |                               0 |                    19 |                           0 |
| Labeled as Upward_shift     |                     0 |                               0 |                             0 |                               0 |                     0 |                          18 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Precision Recall Curve

![Precision Recall Curve](precision_recall_curve.png)



[<< Go back](../README.md)
