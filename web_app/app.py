from flask import Flask, render_template, request

app = Flask(__name__)
FILE_PATH = 'index.html'


# default page of our web-app
@app.route('/')
def home():
    return render_template(FILE_PATH)


# To use the predict button in our web-app
@app.route('/predict', methods=['POST'])
def predict():
    output = 5
    return render_template(FILE_PATH, prediction_text='CO2    Emission of the vehicle is :{}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
