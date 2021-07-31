# %%
import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')
# %%
movies.head()
# %%
movies[movies.duration >= 200]
# %%
movies[(movies.duration >= 200) & (movies.genre == 'Crime')]
# %%
