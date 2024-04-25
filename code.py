import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

flags = pd.read_csv('flag.csv', header=0)
flags = flags.dropna()

data = flags[['Stripes','Colors',"Red", "Green", "Blue", "Gold", "White", "Black", "Orange", "Circles", "Crosses","Saltires","Quarters","Sunstars", "Crescent","Triangle", "Animate", "Icon", "Text"]]
labels = flags[['Name']]

classifier = DecisionTreeClassifier(max_depth=194, random_state=1)
classifier.fit(data, labels)

new_data_point = [3,5,1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1,0]

predicted_country = classifier.predict([new_data_point])

print("Predicted country:", predicted_country)
#type:ignore