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
    if row["direction"] == "forward": # forward X does two things:
        distance = distance + row["steps"] # It increases your horizontal position by X units.
        depth = depth + (aim * row["steps"]) # It increases your depth by your aim multiplied by X.
    elif row["direction"] == "down": 
        aim = aim + row["steps"] # down X increases your aim by X units
    elif row["direction"] == "up": 
        aim = aim - row["steps"] # up X decreases your aim by X units
    else:
        print("Wrong input for direction")

print(f"Distance: {distance}")
print(f"Depth: {depth}")

print(f"Answer for project: {distance*depth}")