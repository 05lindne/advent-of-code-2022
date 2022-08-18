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
# print(data)

# count values where the calculated difference > 0=
# i.e. consecutive input values increased
print(f"Number of increases: {len(data[data['difference']>0])}")

# for every input value, calculate the sum of the current and preceding 2 values
for input in data['input']:
    data['sum_over_three'] = data['input'] + data['input'].shift(1) + data['input'].shift(2)    

print(data)