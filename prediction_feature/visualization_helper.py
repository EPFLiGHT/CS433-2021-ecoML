import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


def scatterplot(consumption_costs, scores, consumption_costs_rmse, scores_rmse):
    """
    Show the results of the prediction tool.
    Order of algorithms in the 4 lists: Linear, Decision tree, Random forest, Neural network
    Parameters
    ----------
    computation_costs List of estimated consumption costs.
    scores List of estimated f1 scores.
    computation_costs_rmse List of rmse of the consumption predictors.
    scores_rmse List of the rmse of the scores predictors.
    """
    fig, ax = plt.subplots()
    fig.set_size_inches(12, 8)

    colors = ['r', 'g', 'b', 'y']
    algorithms = ['Linear', 'Decision tree', 'Random forest', 'Neural network']
    for i in range(4):
        ellipse = Ellipse(xy=(consumption_costs[i], scores[i]), width=consumption_costs_rmse[i], height=scores_rmse[i],
                          color=colors[i], alpha=0.5, lw=1)
        ax.add_patch(ellipse)
        ax.scatter(x=consumption_costs[i], y=scores[i], label=algorithms[i], color=colors[i])


    # set the limit of the axes to -3,3 both on x and y
    ax.set_xlim(0, max(consumption_costs) + 2 * max(consumption_costs_rmse))
    ax.set_ylim(0, 1)
    ax.set_xlabel('Consumption (mgCO2eq)')
    ax.set_ylabel('F1')
    ax.legend(loc='lower right')
    plt.show()