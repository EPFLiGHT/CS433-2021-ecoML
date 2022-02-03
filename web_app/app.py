import numpy as np
from flask import Flask, render_template, request, abort
from base_repository.prediction_feature.prediction_helper import get_predictions
from werkzeug.utils import secure_filename
import pandas as pd

from base_repository.prediction_feature.prediction_helper import compute_features

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/"


@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/display', methods=['GET', 'POST'])
def display_file():
    if request.method == 'POST':
        target_column = request.form.get('name')
        f = request.files['file']
        df = pd.read_csv(f)
        columns = list(df.columns)
        prediction_features = compute_features(df, columns[-1])
        prediction = get_predictions(prediction_features)
        prediction_consumption = np.vstack(prediction[0]).T
        prediction_f1score = np.vstack(prediction[1]).T
        prediction_consumption[1] = [item for sublist in prediction_consumption[1] for item in sublist]
        prediction_f1score[1] = [item for sublist in prediction_f1score[1] for item in sublist]

    return render_template('content.html', cons_linear=prediction_consumption[1][0],
                           cons_Decision_Tree=prediction_consumption[1][1],
                           cons_Random_Forest=prediction_consumption[1][2],
                           cons_Neural_Network=prediction_consumption[1][3],
                           f1_linear=prediction_f1score[1][0],
                           f1_Decision_Tree=prediction_f1score[1][1],
                           f1_Random_Forest=prediction_f1score[1][2],
                           f1_Neural_Network=prediction_f1score[1][3])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)