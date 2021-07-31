# %%
from sklearn.datasets import load_iris

# %%
iris = load_iris()
type(iris)
# %%
iris.data
# %%
iris.feature_names
# %%
iris.target
# %%
iris.target_names
# %%
X = iris.data
y = iris.target

# %%
from sklearn.neighbors import KNeighborsClassifier
# %%
knn = KNeighborsClassifier(n_neighbors=1)
# %%
knn
# %%
knn.fit(X,y)
# %%
knn.predict([[3, 5, 4, 2]])
# %%
knn = KNeighborsClassifier(n_neighbors=5)
# %%
for i in range(1,26):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X,y)
    print(knn.predict([[3, 5, 4, 2]]))
# %%
