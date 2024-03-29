# -*- coding: utf-8 -*-
"""id3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_rxgQJEEVM2HoKNTbwy-YXetzR1oKVE1
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier  # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split  # Import train_test_split function
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix,classification_report

data = pd.read_csv('id3.csv')
label = LabelEncoder()
for i in data.columns:
    data[i] = label.fit_transform(data[i])
X = data.iloc[:,:-1]
Y = data.iloc[:,-1]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)
print(X_train)
print(X_test)
clf = DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(X_train, Y_train)
Y_pred = clf.predict(X_test)

cm = confusion_matrix(Y_test,Y_pred)
creport = classification_report(Y_test,Y_pred)
print("Confusion matrix:\n\n",cm)
print("Classification report:\n\n",creport)
tree.plot_tree(clf)

