import numpy as np
import pandas as pd

# read data from input file into dataframe
df = pd.read_csv('input.txt', delimiter=" ", header = None)
# assign column names
df.columns = ['direction', 'steps']


aim = 0
depth = 0
distance = 0
# https://statisticsglobe.com/loop-through-index-pandas-dataframe-python
for index, row in df.iterrows():
    if row["direction"] == "forward":
        distance = distance + row["steps"]
        depth = aim * row["steps"]
    elif row["direction"] == "down":
        aim = aim + row["steps"]
    elif row["direction"] == "up":
        aim = aim - row["steps"]
    else:
        print("Wrong input for direction")

print(f"Distance: {distance}")
print(f"Depth: {depth}")