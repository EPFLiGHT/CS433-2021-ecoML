# AutoML Leaderboard

| Best model   | name                                                         | model_type     | metric_type   |   metric_value |   train_time |
|:-------------|:-------------------------------------------------------------|:---------------|:--------------|---------------:|-------------:|
| **the best** | [1_DecisionTree](1_DecisionTree/README.md)                   | Decision Tree  | f1            |       1        |         2.05 |
|              | [2_Linear](2_Linear/README.md)                               | Linear         | f1            |       0.964286 |         1.31 |
|              | [3_Default_NeuralNetwork](3_Default_NeuralNetwork/README.md) | Neural Network | f1            |       0.785714 |         1.47 |
|              | [4_Default_RandomForest](4_Default_RandomForest/README.md)   | Random Forest  | f1            |       1        |         1.81 |
|              | [Ensemble](Ensemble/README.md)                               | Ensemble       | f1            |       1        |         0.17 |

### AutoML Performance
![AutoML Performance](ldb_performance.png)

### AutoML Performance Boxplot
![AutoML Performance Boxplot](ldb_performance_boxplot.png)

### Features Importance
![features importance across models](features_heatmap.png)



### Spearman Correlation of Models
![models spearman correlation](correlation_heatmap.png)

