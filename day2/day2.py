import numpy as np
import pandas as pd

df = pd.read_csv('input.txt', delimiter=" ", header = None)

df.columns = ['direction', 'steps']

print(df)