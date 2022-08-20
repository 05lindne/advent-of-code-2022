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

# does not work
# try distance_down > distance_up:
#     depth = distance_down - distance_up 
# except:
#     print("Distance going down must be larger than distance going up")
    
# print(depth)
