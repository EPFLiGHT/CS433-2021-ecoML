from flask import Flask, render_template, request
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
        f = request.files['file']
        df = pd.read_csv(f)
        columns = list(df.columns)
        prediction_features = compute_features(df, columns[-1])
        prediction = get_predictions(prediction_features)
        print(prediction)
    return render_template('content.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


