# %%
from sklearn.datasets import load_iris

iris = load_iris()
# %%
X = iris.data
y = iris.target
# %%
from sklearn.linear_model import LogisticRegression

lngreg = LogisticRegression()

lngreg.fit(X,y)

lngreg.predict(X)
# %%
y_pred = lngreg.predict(X)

len(y_pred)
# %%
from sklearn import metrics
metrics.accuracy_score(y, y_pred)
# %%
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X,y)
y_pred = knn.predict(X)
print(metrics.accuracy_score(y, y_pred))
# %%
acc_res = []
for i in range(2,26):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X,y)
    y_pred = knn.predict(X)
    acc_res.append(metrics.accuracy_score(y,y_pred))
# %%
from matplotlib import pyplot
pyplot.plot(acc_res)
# %%
