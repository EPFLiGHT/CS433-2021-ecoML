import pickle

models_directory = '/prediction_feature/models/'


def get_predictions(x):
    """

    Parameters
    ----------
    x vector representing the dataset on which to predict consumption and f1 for the different classification algorithms

    Returns
    -------

    """
    algorithms = ['Linear', 'Decision_Tree', 'Random_Forest', 'Neural_Network']

    consumptions_list = []
    scores_list = []
    for algorithm in algorithms:
        consumption_model = pickle.load(open('consumption_model_' + algorithm + '.sav', 'rb'))
        score_model = pickle.load(open('model_' + algorithm + '.sav', 'rb'))
        consumption_prediction = consumption_model.predict(x)
        score_prediction = score_model.predict(x)
        consumptions_list.append(consumption_prediction)
        scores_list.append(score_prediction)

    consumption_rmse_list = [300, 300, 300, 300]
    score_rmse_list = [0.2, 0.2, 0.2, 0.2]

    return consumptions_list, scores_list, consumption_rmse_list, score_rmse_list
