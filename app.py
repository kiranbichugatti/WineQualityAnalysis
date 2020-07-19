# -*- coding: utf-8 -*-
"""
Created on 

@author: 
"""
import os
import pandas as pd

import json

from flask import Flask
from flask_restful import Api, Resource, request
from flask import Flask, request, render_template
import joblib


port = int(os.getenv('PORT', '5000'))

app = Flask(__name__)
api = Api(app)

# argument parsing
#parser = reqparse.RequestParser()
#parser.add_argument('query')


class PredictRegression(Resource):
    def get(self):
        model_path = 'lib/models/logisticRegressionModel.pkl'
        with open(model_path, 'rb') as f:
            regression_model = joblib.load(f)
                
        # get the query parameters
        #param = request.args.get('param')
        params = request.args

        independents=pd.DataFrame(params,index=[0])
              
        # make a prediction
        predictions = regression_model.predict(independents)
       
        # create JSON object
        #pd.DataFrame(predictions, columns=['Prediction'])
        output = pd.DataFrame(predictions, columns=['Prediction']).to_json(orient='table')
        output=json.loads(output)
        
        return output
    
    def post(self):
        model_path = 'lib/models/logisticRegressionModel.pkl'
        with open(model_path, 'rb') as f:
            regression_model = joblib.load(f)
                
        # get the form data
        params = request.form

        independents=pd.DataFrame(params,index=[0])
              
        # make a prediction
        predictions = regression_model.predict(independents)
       
        # create JSON object
        #pd.DataFrame(predictions, columns=['Prediction'])
        output = pd.DataFrame(predictions, columns=['Prediction']).to_json(orient='table')
        output=json.loads(output)
        
        return output





# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictRegression, '/regression')

@app.route('/')
def form():
    return render_template("form.html")



if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=port)