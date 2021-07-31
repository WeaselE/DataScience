# %%
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target
# %%
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X,y)

X_new = [[3,5,4,2], [5,4,3,2]]
knn.predict(X_new)
# %%
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(solver='liblinear')
logreg.fit(X,y)
logreg.predict(X_new)
# %%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=4)
# %%
X_train.shape
# %%
X_test.shape
# %%
y_train.shape
# %%
y_test.shape
# %%
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
# %%
from sklearn.metrics import accuracy_score
y_pred = logreg.predict(X_test)
print(accuracy_score(y_test, y_pred))
# %%
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(accuracy_score(y_test, y_pred))
# %%
scores = []
for k in range(1,26):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores.append(accuracy_score(y_test, y_pred))
# %%
scores
# %%
import matplotlib.pyplot as plt
plt.plot(scores)
# %%
