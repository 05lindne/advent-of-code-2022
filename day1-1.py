import pandas as pd
import numpy as np

# read data into dataframe
data = pd.read_csv('input.txt',delimiter="\t", header = None)
# assign column name
data.columns = ['input']
# print(data)

# calculate difference between two consecutive values in 'input' column
# and write result into new column named 'difference'
data['difference'] = data['input'].diff()
print(data)



#create DataFrame
df2 = pd.DataFrame({'period': [1, 2, 3, 4, 5, 6, 7, 8],
                   'sales': [12, 14, 15, 13, 18, 20, 19, 24],
                   'returns': [2, 2, 3, 3, 5, 4, 4, 6]})

#find difference between each current row and the previous row
df2['sales_diff'] = df2['sales'].diff()

#filter for rows where difference is less than zero
# df2 = df2[df2['sales_diff']<0]

#view DataFrame
print(df2)
