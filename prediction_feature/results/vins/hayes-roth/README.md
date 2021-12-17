# AutoML Leaderboard

| Best model   | name                                                         | model_type     | metric_type   |   metric_value |   train_time |
|:-------------|:-------------------------------------------------------------|:---------------|:--------------|---------------:|-------------:|
|              | [1_DecisionTree](1_DecisionTree/README.md)                   | Decision Tree  | f1            |       0.666667 |         2.49 |
|              | [2_Linear](2_Linear/README.md)                               | Linear         | f1            |       0.533333 |         1.34 |
|              | [3_Default_NeuralNetwork](3_Default_NeuralNetwork/README.md) | Neural Network | f1            |       0.566667 |         1.42 |
| **the best** | [4_Default_RandomForest](4_Default_RandomForest/README.md)   | Random Forest  | f1            |       0.8      |         1.86 |
|              | [Ensemble](Ensemble/README.md)                               | Ensemble       | f1            |       0.8      |         0.16 |

### AutoML Performance
![AutoML Performance](ldb_performance.png)

### AutoML Performance Boxplot
![AutoML Performance Boxplot](ldb_performance_boxplot.png)

### Features Importance
![features importance across models](features_heatmap.png)



### Spearman Correlation of Models
![models spearman correlation](correlation_heatmap.png)

