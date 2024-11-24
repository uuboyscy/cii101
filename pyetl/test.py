import pandas as pd


df = pd.DataFrame(columns=["Name", "Age", "Height"])
df.loc[0] = ["Allen", 22, 175]

print(df)