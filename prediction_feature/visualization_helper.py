import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


def scatterplot(computation_costs, scores, computation_costs_rmse, scores_rmse):
    fig, ax = plt.subplots()
    fig.set_size_inches(12, 8)

    colors = ['r', 'g', 'b', 'y']
    algorithms = ['Linear', 'Decision tree', 'Random forest', 'Neural network']
    for i in range(4):
        ellipse = Ellipse(xy=(computation_costs[i], scores[i]), width=computation_costs_rmse[i], height=scores_rmse[i],
                          color=colors[i], alpha=0.5, lw=1)
        ax.add_patch(ellipse)
        ax.scatter(x=computation_costs[i], y=scores[i], label=algorithms[i], color=colors[i])


    # set the limit of the axes to -3,3 both on x and y
    ax.set_xlim(0, max(computation_costs) + 2 * max(computation_costs_rmse))
    ax.set_ylim(0, 1)
    ax.set_xlabel('Computation cost')
    ax.set_ylabel('F1')
    ax.legend(loc='lower right')
    plt.show()

scatterplot([100, 1500, 900, 1200], [0.8, 0.9, 0.7, 0.6], [100, 75, 200, 175], [0.2, 0.3, 0.1, 0.5])