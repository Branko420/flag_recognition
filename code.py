import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from flask import Flask, render_template, request, jsonify, session
import secrets

secret_key=secrets.token_hex(32)
app = Flask(__name__)
app.secret_key = secret_key

flags = pd.read_csv('flag.csv', header=0).dropna()

data = flags[['Stripes','Colors',"Red", "Green", "Blue", "Gold", "White", "Black", "Orange", "Circles", "Crosses","Saltires","Quarters","Sunstars","Crescent","Triangle", "Animate", "Icon", "Text"]]
labels = flags[['Name']]

classifier = DecisionTreeClassifier(max_depth=194, random_state=1)
classifier.fit(data, labels)

@app.route('/')
def index():
    return render_template('adding_values_to_predict_with.html')

@app.route('/json_to_predict_with', methods=["POST"])
def json_post():
    if request.method== 'POST':
        json = request.get_json() 
        data_to_predict = []
        for key, values in json.items():
            data_to_predict.append(values)
        prediction = classifier.predict([data_to_predict])
        session['predicted_flag'] = prediction[0]
        return jsonify({'predict': prediction[0]}), 200
    return jsonify({'error':'invalid request method'}), 405


@app.route('/predict', methods=["GET"])
def predict():
    if request.method=="GET":
        
        predicted_coutry = session['predicted_flag']
        print(predicted_coutry)
        return render_template('predicted_flag_page.html', prediction = predicted_coutry )

if __name__=="__main__":
    app.run(debug=True)
#type:ignore