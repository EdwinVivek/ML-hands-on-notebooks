import matplotlib.pyplot as plt
from sklearn import datasets, cluster
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import pandas as pd

#Load data
iris = datasets.load_iris()

#Create data frame
iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
iris_df['response'] = iris.target

#convert to categorical
iris_df['response'] = iris_df['response'].astype('category')
iris_df.response.cat.categories = iris.target_names

#Split data
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=1, test_size=0.4)


#Cross validation
kf = KFold(n_splits = 5)

for train_index, test_index in kf.split(iris.data):
 print("TRAIN:", train_index, "TEST:", test_index)
 X_train, X_test = iris.data[train_index], iris.data[test_index]
 print("Xtr:", X_train, "Xtes:", X_test)

#plot target data
sns.countplot(x=iris_df['response'], data = iris_df)
plt.xticks(rotation=90)
plt.show()
 
#plot entire data
fig, ax = plt.subplots()
color = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
for i,col, lab in zip(range(len(iris.data[0])), color,  iris.feature_names):
	ax.scatter(iris.target, iris.data[:,i], c=col, label=lab)


#K-means
kmm = cluster.KMeans(3)
kmm.fit(iris.data)
centroids= kmm.cluster_centers_

#plot centroids
for j, lab in zip(range(len(centroids)+1), iris.feature_names):
    ax.scatter([0,1,2], centroids[:,j], marker='*', s=300, c=color[j], label='cent_'+lab)


ax.set_xticks([0,1,2])
ax.set_xticklabels(iris.target_names)
ax.legend()
plt.show()

#model evaluation
ac_score = accuracy_score(iris.target, kmm.labels_)
print("Accuracy score:", ac_score)
mat = confusion_matrix(iris.target, kmm.labels_)

sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=iris.target_names,
            yticklabels=iris.target_names)
plt.show()

#predict
pred = kmm.predict(iris.data)

fig, ax = plt.subplots()
ax.plot(iris.target, 'bo')
ax.plot(pred, 'r+')
plt.show()


fig, ax = plt.subplots()
for i,col, lab in zip(range(len(iris.data[0])), color,  iris.feature_names):
	ax.scatter(iris.target, iris.data[:,i], c=pred, label=lab)
	
plt.show()
