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

@app.route('/predict',methods=['post','get'])
def predict():
    model = joblib.load('pipeline.pkl')
    to_pred = requrest.form.to_dict()
    to_pred = list(to_pred.values)
    to_pred = np.array(list(map(float,to_pred))).reshape(1,-1)
    print(to_pred)
    y_bar = model.predict(to_pred)
    return jsonify ({'prediction':list(y_bar)})
    
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080)
    app.run(port=8000)
