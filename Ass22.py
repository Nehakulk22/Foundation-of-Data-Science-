import pandas as pd
import numpy as np


df2= pd.read_excel("Book2.xlsx")
print("\n---------Excel----------")

print("Tail() Function\n")
print(df2.tail())

print("Type:", type(df2))
print("Columns:", list(df2.columns))
print("Index:", df2.index.tolist())
print("\nInfo:")
df2.info()

print("\nDescribe:")
print(df2.describe())

print("\nShape (rows, columns):", df2.shape)

# loc: label-based selection
print("loc example (rows 0-2, specific columns):")
print(df2.loc[0:2, ["product_category", "revenue"]])

# iloc: position-based selection
print("\niloc example (first 3 rows, first 3 columns):")
print(df2.iloc[0:3, 0:3])

# Boolean indexing: filter rows where quantity is greater than 5
print("\nBoolean indexing (quantity > 5):")
print(df2[df2["quantity"] > 5])