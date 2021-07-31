# %%
import pandas as pd
# %%
ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo.head())
print(ufo['City'])

# %%
print(type(ufo['City']))