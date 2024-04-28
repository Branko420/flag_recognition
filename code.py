import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

flags = pd.read_csv('flag.csv', header=0).dropna()

data = flags[['Stripes','Colors',"Red", "Green", "Blue", "Gold", "White", "Black", "Orange", "Circles", "Crosses","Saltires","Quarters","Sunstars","Crescent","Triangle", "Animate", "Icon", "Text"]]
labels = flags[['Name']]

classifier = DecisionTreeClassifier(max_depth=194, random_state=1)
classifier.fit(data, labels)

@app.route('/')
def index():
    return render_template("adding_values_to_predict_with.html")

#data i want to predict with
new_data_point = [[3,5,1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1,0]]

predicted_probability = classifier.predict_proba(new_data_point)
#geting the top 3 predictions 
top_indices =  np.argpartition(predicted_probability, -3, axis=1)[:,-3:]
top_three_countries = [[flags.iloc[i]["Name"] for i in indice] for indice in top_indices]

print("Predicted country:", top_three_countries[0][::-1])
#type:ignore