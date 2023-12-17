from sklearn.datasets import  load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

x=load_iris().data
print(x)
y=load_iris().target