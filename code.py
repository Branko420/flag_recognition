from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split

flags = pd.read_csv('flag.csv', header=0)
data = flags[["Red", "Green", "Blue", "Gold", "White", "Black", "Orange", "Circles", "Crosses","Saltires","Quarters","Sunstars", "Crescent","Triangle"]]
labels = flags[['Name']]

data_train, data_test, labels_train, labels_test=train_test_split(data, labels, random_state=1, test_size=0.2)

classifier = DecisionTreeClassifier(max_depth=5, random_state=1)
classifier.fit(data_train, labels_train)


print(classifier.score(data_test, labels_test))
 # type: ignore