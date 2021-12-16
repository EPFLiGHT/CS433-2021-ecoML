# Summary of 2_Default_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 16
- **learning_rate**: 0.05
- **num_class**: 6
- **explain_level**: 1

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
f1

## Training time

235.3 seconds

### Metric details
|           |          1.0 |          2.0 |          3.0 |          4.0 |          5.0 |          7.0 |   accuracy |     macro avg |   weighted avg |   logloss |
|:----------|-------------:|-------------:|-------------:|-------------:|-------------:|-------------:|-----------:|--------------:|---------------:|----------:|
| precision |     0.967483 |     0.914026 |     0.881923 |     0.562345 |     0.786318 |     0.869178 |   0.860123 |      0.830212 |       0.861504 |  0.402737 |
| recall    |     0.952313 |     0.907605 |     0.925525 |     0.589468 |     0.759301 |     0.843918 |   0.860123 |      0.829689 |       0.860123 |  0.402737 |
| f1-score  |     0.959838 |     0.910804 |     0.903198 |     0.575587 |     0.772573 |     0.856362 |   0.860123 |      0.829727 |       0.860586 |  0.402737 |
| support   | 44771        | 20499        | 39624        | 18079        | 20723        | 43804        |   0.860123 | 187500        |  187500        |  0.402737 |


## Confusion matrix
|                |   Predicted as 1.0 |   Predicted as 2.0 |   Predicted as 3.0 |   Predicted as 4.0 |   Predicted as 5.0 |   Predicted as 7.0 |
|:---------------|-------------------:|-------------------:|-------------------:|-------------------:|-------------------:|-------------------:|
| Labeled as 1.0 |              42636 |                253 |                775 |                238 |                845 |                 24 |
| Labeled as 2.0 |                169 |              18605 |                 53 |                475 |               1110 |                 87 |
| Labeled as 3.0 |                340 |                135 |              36673 |               1776 |                377 |                323 |
| Labeled as 4.0 |                185 |                113 |               3103 |              10657 |                718 |               3303 |
| Labeled as 5.0 |                670 |               1200 |                257 |               1034 |              15735 |               1827 |
| Labeled as 7.0 |                 69 |                 49 |                722 |               4771 |               1226 |              36967 |

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
