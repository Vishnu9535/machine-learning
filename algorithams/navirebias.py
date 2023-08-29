from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics


iris_data= load_iris()
X= iris_data['data']
y=iris_data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
gnb = GaussianNB()
gnb.fit(X_train,y_train)
y_pred = gnb.predict(X_test)
print(y_pred)
print(y_test)
print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)