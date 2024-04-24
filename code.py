from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np

flags = pd.read_csv('flag.csv', header=0)
data = flags[["Red", "Green", "Blue", "Gold", "White", "Black", "Orange", "Circles", "Crosses","Saltires","Quarters","Sunstars", "Crescent","Triangle"]]
labels = flags[['Landmass']]

classifier = DecisionTreeClassifier(max_depth=5, random_state=1)
classifier.fit(data, labels)

predicted_probabilities = classifier.predict_proba([[1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

top_indices = np.argpartition(predicted_probabilities, -3, axis=1)[:, -3:]

top_countries = [[flags.iloc[index]['Name'] for index in indices] for indices in top_indices]

print("Top 3 countries:", top_countries)
predicted_point=classifier.predict([[1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
 # type: ignore