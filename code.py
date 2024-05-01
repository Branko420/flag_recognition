import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

flags = pd.read_csv('flag.csv', header=0).dropna()

data = flags[['Stripes','Colors',"Red", "Green", "Blue", "Gold", "White", "Black", "Orange", "Circles", "Crosses","Saltires","Quarters","Sunstars","Crescent","Triangle", "Animate", "Icon", "Text"]]
labels = flags[['Name']]

classifier = DecisionTreeClassifier(max_depth=194)
classifier.fit(data, labels)

@app.route('/')
def index():
    return render_template('adding_values_to_predict_with.html')

@app.route('/predict', methods=['POST'])
def predict():
    json = request.get_json()
    print(json)
    new_data_point=[]
    for key, value in json.items():
        new_data_point.append(value)
    print(new_data_point)
    new_data_point = [new_data_point]

    predict = classifier.predict(new_data_point)
    print(predict)
    return json
if __name__=="__main__":
    app.run(debug=True)
#type:ignore