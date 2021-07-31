 # %%

import pandas as pd

# Source: http://bit.ly/chiporders
orders = pd.read_table('tabular_data/chipotle.tsv', )

print(orders.head())
# %%
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols)
print(users.head())
# %%
