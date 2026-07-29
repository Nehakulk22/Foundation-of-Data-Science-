import pandas as pd
import numpy as np

df = pd.read_csv("salary_data (1).csv")

print("Head() Function\n")
print(df.head())

print("Type:", type(df))
print("Columns:", list(df.columns))
print("Index:", df.index.tolist())

print("\nInfo:")
df.info()

print("\nDescribe:")
print(df.describe())

print("\nShape (rows, columns):", df.shape)

# loc: label-based selection
print("loc example (rows 0-2, specific columns):")
print(df.loc[0:2, ["YearsExperience", "Salary"]])

# iloc: position-based selection
print("\niloc example (first 3 rows, first 3 columns):")
print(df.iloc[0:3, 0:3])

# Boolean indexing: filter rows where YearsExperience is greater than 5
print("\nBoolean indexing (YearsExperience > 5):")
print(df[df["YearsExperience"] > 5])