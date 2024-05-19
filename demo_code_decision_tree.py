import pandas as pd

from sklearn.tree import DecisionTreeClassifier

flags = pd.read_csv('flag.csv', header=0).dropna()

data = flags[['Bars','Stripes','Colors',"Red", "Green", "Blue", "Gold", "White", "Black", "Orange", "Circles", "Crosses","Saltires","Quarters","Sunstars","Crescent","Triangle", "Icon", "Animate", "Text"]]
labels = flags[['Name']]

classifier = DecisionTreeClassifier(max_depth=20,random_state=42)
classifier.fit(data,labels)

def predict_flag(prediction =[]):
    prediction = classifier.predict([prediction])
    return prediction 

#print(predict_flag([0, 2, 5, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]))