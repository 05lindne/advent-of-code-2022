import pandas as pd
import numpy as np

# read data into dataframe
data = pd.read_csv('input.txt',delimiter="\t", header = None)
# assign column name
data.columns = ['input']
# print(data)

# calculate difference between two consecutive input values in 'input' column
# and write result into new column named 'difference'
data['difference'] = data['input'].diff()
print(data)

# count values where the calculated difference > 0=
# i.e. consecutive input values increased
print(f"Number of increases: {len(data[data['difference']>0])}")
