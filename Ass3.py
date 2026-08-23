
import numpy as np
import pandas as pd
from scipy import stats
from collections import Counter

ss = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

print(ss.head())
print(ss.describe())

profit=ss['Profit']

profit_list = list(profit)

manual_mean = sum(profit_list) / len(profit_list)

sorted_profit = sorted(profit_list)
n = len(sorted_profit)

if n % 2 == 0:
    manual_median = (sorted_profit[n // 2 - 1] + sorted_profit[n // 2]) / 2
else:
    manual_median = sorted_profit[n // 2]

frequency = Counter(profit_list)
manual_mode = frequency.most_common(1)[0][0]

print("Manual Mean / Average of Profit:", manual_mean)
print("Manual Median of Profit:", manual_median)
print("Manual Mode of Profit:", manual_mode)

profit_array = np.array(profit_list)

numpy_mean = np.mean(profit_array)
numpy_median = np.median(profit_array)

values, counts = np.unique(profit_array, return_counts=True)
numpy_mode = values[np.argmax(counts)]

print("NumPy Mean / Average of Profit:", numpy_mean)
print("NumPy Median of Profit:", numpy_median)
print("NumPy Mode of Profit:", numpy_mode)
pandas_mean = ss["Profit"].mean()
pandas_median = ss["Profit"].median()
pandas_mode = ss["Profit"].mode()[0]

print("Pandas Mean / Average of Profit:", pandas_mean)
print("Pandas Median of Profit:", pandas_median)
print("Pandas Mode of Profit:", pandas_mode)
# Distribution / Skewness of Profit

profit = ss["Profit"].dropna()

mean_val = profit.mean()
median_val = profit.median()
skewness = profit.skew()

print("Mean of Profit:", mean_val)
print("Median of Profit:", median_val)
print("Skewness of Profit:", skewness)

if mean_val > median_val:
    print("Distribution is right / positively skewed")
elif mean_val < median_val:
    print("Distribution is left / negatively skewed")
else:
    print("Distribution is approximately symmetric")