# %%
import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')

movies.head()
# %%
movies.describe()
# %%
movies.shape
# %%
movies.dtypes
# %%
movies.describe(include=['object'])
# %%
