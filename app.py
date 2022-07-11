import joblib
import flask
import gunicorn
from flask import Flask, jsonify, request
import numpy as np
import joblib

app = flask(__name__)

@app.route('/')
def homepage():
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
    