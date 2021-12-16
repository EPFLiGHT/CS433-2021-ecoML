# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                   |   Weight |
|:------------------------|---------:|
| 2_Default_NeuralNetwork |        1 |

### Metric details
|           |          1 |          2 |          3 |          4 |          5 |          6 |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|------------:|---------------:|----------:|
| precision |   0.997877 |   0.990842 |   0.990132 |   0.97541  |   0.981067 |   0.991176 |    0.98773 |    0.987751 |       0.987808 | 0.0684019 |
| recall    |   0.989474 |   0.989031 |   0.961661 |   0.991667 |   0.996503 |   0.98827  |    0.98773 |    0.986101 |       0.98773  | 0.0684019 |
| f1-score  |   0.993658 |   0.989936 |   0.975689 |   0.983471 |   0.988725 |   0.989721 |    0.98773 |    0.986867 |       0.987718 | 0.0684019 |
| support   | 475        | 547        | 313        | 360        | 572        | 341        |    0.98773 | 2608        |    2608        | 0.0684019 |


## Confusion matrix
|              |   Predicted as 1 |   Predicted as 2 |   Predicted as 3 |   Predicted as 4 |   Predicted as 5 |   Predicted as 6 |
|:-------------|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| Labeled as 1 |              470 |                0 |                0 |                5 |                0 |                0 |
| Labeled as 2 |                0 |              541 |                1 |                2 |                3 |                0 |
| Labeled as 3 |                0 |                5 |              301 |                0 |                7 |                0 |
| Labeled as 4 |                0 |                0 |                0 |              357 |                0 |                3 |
| Labeled as 5 |                0 |                0 |                2 |                0 |              570 |                0 |
| Labeled as 6 |                1 |                0 |                0 |                2 |                1 |              337 |

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
