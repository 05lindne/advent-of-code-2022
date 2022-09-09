import numpy as np
import pandas as pd

# read data from input file into dataframe
df = pd.read_csv('input.txt', delimiter=" ", header = None)

# assign column names
df.columns = ['direction', 'steps']


# sum up all values in the steps column, where the entries in the direction column are the same
distance_forward = sum(df.loc[df.direction == 'forward'].steps)
distance_up = sum(df.loc[df.direction == 'up'].steps)
distance_down = sum(df.loc[df.direction == 'down'].steps)
print(f"distance_forward = {distance_forward}")
print(f"distance_up = {distance_up}")
print(f"distance_down = {distance_down}")


if distance_down > distance_up:
    depth = distance_down - distance_up 
else:
    print("Distance going down must be larger than distance going up")
    exit()
    
print(f"Depth = {depth}")
print(f"Horizontal distance = {distance_forward}")
print(f"Depth multiplied by horizontal distance: {depth*distance_forward}")
