import numpy as np
from sklearn import datasets
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

knn = KNeighborsClassifier(algorithm='auto', leaf_size=30,
                           metric='minkowski', metric_params=None, n_jobs=1,
                           n_neighbors=3, p=2, weights='uniform')

df = pd.read_csv("top_fifty.csv")

df = df.drop(columns=['p-value'])
df = df.drop(columns=['gene_accession_number'])
flipped = df.transpose()
values = flipped[0].values
flipped = flipped.drop(columns=[0])

# print(flipped.head())
# print(values)

knn.fit(flipped, values)

tf = pd.read_csv("top_fifty_test.csv")

tf = tf.drop(columns=['gene_accession_number'])
tf = tf.drop(columns=['p-value'])
tf = tf.transpose()
testValues = tf[0].values
tf = tf.drop(columns=[0])
# print(tf.head())
# tf = tf.drop(tf.ix[:, 53:].columns, axis = 1)
# print(trueValues)

print("Predicted:")
print(knn.predict(tf))
print("Actual:")
print(testValues)