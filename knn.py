import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(algorithm='auto', leaf_size=30,
                           metric='minkowski', metric_params=None, n_jobs=1,
                           n_neighbors=3, p=2, weights='uniform')

df = pd.read_csv("top_fifty.csv")

df = df.drop(columns=['p-value'])
df = df.drop(columns=['gene_accession_number'])
flipped = df.transpose()
values = flipped[0].values
flipped = flipped.drop(columns=[0])

knn.fit(flipped, values)

tf = pd.read_csv("top_fifty_test.csv")

tf = tf.drop(columns=['gene_accession_number'])
tf = tf.drop(columns=['p-value'])
tf = tf.transpose()
testValues = tf[0].values
tf = tf.drop(columns=[0])

print("Predicted:")
print(knn.predict(tf))
print("Actual:")
print(testValues)