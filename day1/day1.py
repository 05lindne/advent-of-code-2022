import pandas as pd
import numpy as np

# read data from input file into dataframe
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
increases = len(data[data['difference']>0])
print(f"Number of increases: {increases}")

# for every input value, calculate the sum of the current and preceding 2 values
for input in data['input']:
    data['sum_over_three'] = data['input'] + data['input'].shift(1) + data['input'].shift(2)    
# print(data)

data['difference_over_three'] = data['sum_over_three'].diff()
print(data)

increases_over_three = len(data[data['difference_over_three']>0])
print(f"Number of increases_over_three: {increases_over_three}")