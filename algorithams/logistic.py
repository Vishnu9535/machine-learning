import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

titanic_data = pd.read_csv("train.csv")
y = titanic_data["Survived"]
cclumns_to_drop = ['Survived','Name','Sex','Age','Ticket','Fare','Cabin','Embarked']
x = titanic_data.drop(cclumns_to_drop,axis=1)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state = 1)
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
LogisticRegression(C=1.0, class_weight=None, dual= False,
                   fit_intercept=True, intercept_scaling=1,
                   max_iter = 100, multi_class='ovr', n_jobs=1,
                   penalty='12',random_state=None, solver = 'liblinear',
                   tol = 0.0001,verbose=0, warm_start=False)
predictions = logmodel.predict(X_test)
# print(predictions)
classification_report(y_test,predictions)
confusion_matrix(y_test,predictions)