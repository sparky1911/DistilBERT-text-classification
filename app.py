from flask import Flask, request, jsonify
import distilbert_model as model
from flask_cors import CORS
import numpy as np
from flask import Flask, request,render_template
from flask_cors import CORS
import os
import flask
import urllib
from flask_json import FlaskJSON, JsonError, json_response, as_json
app = Flask(__name__)
CORS(app)
app=flask.Flask(__name__,template_folder='templates')

@app.route('/')
def main():
    return "working"

# get the json data
@app.route("/predict", methods=['GET','POST'])
def predict():
	tx = request.get_json(force = True)
	text = tx['text']

	sent = model.predict(text)

	return jsonify(label = sent)



if __name__=="__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)
