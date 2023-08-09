import pandas as pd

df = pd.read_csv('/file/path.csv')
df = df.fillna(0)

df["Total Owed"] = df["Total Owed"].str.replace(',','').astype(float)


print("The total amout of money you spend on amazon is: $",df["Total Owed"].sum())
print("The highest amount you spent was: $",df["Total Owed"].max())
