# %%
import pandas as pd
# %%
movies = pd.read_csv('http://bit.ly/imdbratings')
# %%
movies.head()
# %%
movies.sort_values(['genre', 'duration'])