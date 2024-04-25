import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

flags = pd.read_csv('flag.csv', header=0)
flags = flags.dropna()

data = flags[['Stripes','Colors',"Red", "Green", "Blue", "Gold", "White", "Black", "Orange", "Circles", "Crosses","Saltires","Quarters","Sunstars", "Crescent","Triangle", "Animate", "Icon", "Text"]]
labels = flags[['Name']]

classifier = DecisionTreeClassifier(max_depth=194, random_state=1)
classifier.fit(data, labels)

new_data_point = [[3,5,1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1,0]]

predicted_country = classifier.predict_proba(new_data_point)
top_indices =  np.argpartition(predicted_country, -3, axis=1)[:,-3:]
top_three_countries = [[flags.iloc[i]["Name"] for i in indice] for indice in top_indices]

print("Predicted country:", top_three_countries[0][::-1])
#type:ignore