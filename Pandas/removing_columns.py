# %%
import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')

# %%
movies.head()
# %%
movies = movies.drop('content_rating', axis=1)
# %%
movies.head()