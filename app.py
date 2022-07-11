import joblib
import flask
import gunicorn
from flask import Flask, jsonify, request
import numpy as np
import joblib

app = Flask(__name__)

# @app.route('/')
# def helo_world():
#     return "hello world"

@app.route('/')
def input():
    return flask.render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    lr = joblib.load('pipeline.pkl')
    to_predict_list = request.form.to_dict()
    to_predict_list = list(to_predict_list.values())
    to_predict_list = np.array(list(map(float, to_predict_list))).reshape(1, -1)
    print(to_predict_list)
    prediction = lr.predict(to_predict_list)
    print(prediction)
    return jsonify({'prediction': list(prediction)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

    