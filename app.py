from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import pandas as pd
import json


import traceback


app = Flask(__name__)

    
@app.route('/api/', methods=['POST'])
def makecalc():
	j_data = request.get_json()

	prediction = np.array2string(model.predict(j_data))
	
	return jsonify(prediction)

@app.route('/predict', methods=['POST'])
def predict():
    
    try:
        json_ = request.json
        print(json_)
        # pending - get input data in suitable format
        prediction = list(model.predict(np.reshape(json_, (1,-1))))
        return jsonify({'prediction': str(prediction)})

    except:
        return jsonify({'trace': traceback.format_exc()})
    

@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"


if __name__ == '__main__':

    modelfile = 'final_prediction.pickle'    

    model = p.load(open(modelfile, 'rb'))
    
    app.run(debug=True,host='0.0.0.0')