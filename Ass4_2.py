import pandas as pd
import numpy as np
#without Built in Function

# City A temperatures
city_a = [25, 28, 30, 27, 26, 29, 31]

# City B temperatures
city_b = [20, 35, 25, 40, 18, 32, 22]

# Find minimum and maximum manually
min_a = city_a[0]
max_a = city_a[0]

for x in city_a:
    if x < min_a:
        min_a = x
    if x > max_a:
        max_a = x

min_b = city_b[0]
max_b = city_b[0]

for x in city_b:
    if x < min_b:
        min_b = x
    if x > max_b:
        max_b = x

# Calculate range
range_a = max_a - min_a
range_b = max_b - min_b

print("Range - City A:", range_a)
print("Range - City B:", range_b)

print()
print("----------------------------------------------")
print()

#With Built in Function
# Load dataset
df = pd.read_csv("CityTemperatures.csv")

print(df.head())
print()
print(df.describe())
print()
# Range using built-in functions
range_a = df['City_A'].max() - df['City_A'].min()
range_b = df['City_B'].max() - df['City_B'].min()

print("Range - City A:", range_a)
print("Range - City B:", range_b)

# Variance
var_a = df['City_A'].var()
var_b = df['City_B'].var()

print("Variance - City A:", var_a)
print("Variance - City B:", var_b)

# Standard Deviation
std_a = df['City_A'].std()
std_b = df['City_B'].std()

print("Std Dev - City A:", std_a)
print("Std Dev - City B:", std_b)

# Coefficient of Variation
cv_a = (std_a / df['City_A'].mean()) * 100
cv_b = (std_b / df['City_B'].mean()) * 100

print("CV% - City A:", cv_a)
print("CV% - City B:", cv_b)

# Interpretation
if std_a < std_b:
    print("City A has more consistent temperatures than City B")
else:
    print("City B has more consistent temperatures than City A")
    
