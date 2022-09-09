import pandas as pd

df = pd.DataFrame({'x1':['a', 'b', 'c', 'd'], 'x2':['w', 'x', 'y', 'z']})
print(df)                                        # Print pandas DataFrame

for index, row in df.iterrows():
    if row["x1"] == "a":
        print("row a")
    elif row["x1"] == "b":
        print("row b") 
    elif row["x1"] == "c":
        print("row c")
    else:
        print("Wrong input for direction")