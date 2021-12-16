# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                   |   Weight |
|:------------------------|---------:|
| 3_Default_NeuralNetwork |        1 |

### Metric details
|           |        3 |   4 |          5 |          6 |         7 |   8 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|---------:|----:|-----------:|-----------:|----------:|----:|-----------:|------------:|---------------:|----------:|
| precision | 0.666667 |   0 |   0.641892 |   0.59292  |  0.473684 |   0 |   0.603279 |    0.395861 |       0.570345 |   1.03538 |
| recall    | 0.8      |   0 |   0.753968 |   0.553719 |  0.473684 |   0 |   0.603279 |    0.430229 |       0.603279 |   1.03538 |
| f1-score  | 0.727273 |   0 |   0.693431 |   0.57265  |  0.473684 |   0 |   0.603279 |    0.411173 |       0.584588 |   1.03538 |
| support   | 5        |  10 | 126        | 121        | 38        |   5 |   0.603279 |  305        |     305        |   1.03538 |


## Confusion matrix
|              |   Predicted as 3 |   Predicted as 4 |   Predicted as 5 |   Predicted as 6 |   Predicted as 7 |   Predicted as 8 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 3 |                4 |                0 |                1 |                0 |                0 |                0 |
| Labeled as 4 |                0 |                0 |                8 |                1 |                1 |                0 |
| Labeled as 5 |                1 |                0 |               95 |               27 |                3 |                0 |
| Labeled as 6 |                1 |                0 |               39 |               67 |               14 |                0 |
| Labeled as 7 |                0 |                0 |                5 |               15 |               18 |                0 |
| Labeled as 8 |                0 |                0 |                0 |                3 |                2 |                0 |

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
