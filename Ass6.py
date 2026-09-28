import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
import pandas as pd

# 1. Load data
df = pd.read_csv("COVID clinical trials.csv")

# 2. Select trial status
data = df['Status'].dropna()

# 3. Take first 20 clinical trials
data = data.head(20)

# 4. Convert status into binary outcomes
# Completed = Success
# Other status = Failure
success = (data.str.lower() == 'completed').astype(int)

# 5. Define parameters
n = len(success)
p = np.mean(success)

print('Number of Trials:', n)
print('Probability of Success:', p)

# 6. Generate possible number of successes
x = np.arange(0, n + 1)

# 7. Calculate PMF and CDF
pmf = binom.pmf(x, n, p)
cdf = binom.cdf(x, n, p)

# 8. Calculate mean and standard deviation
mean = n * p
variance = n * p * (1 - p)
std_dev = np.sqrt(variance)

print('Mean:', mean)
print('Variance:', variance)
print('Standard Deviation:', std_dev)

## 9. Plot the Binomial Distribution
plt.figure(figsize=(8, 5))

plt.bar(
    x, pmf,
    color='#FFDCDC',
    edgecolor='#D9A3A3',
    alpha=0.9,
    label='Probability'
)

plt.plot(
    x, pmf,
    color='#B76E79',
    marker='o',
    linewidth=2,
    label='Binomial Distribution'
)

plt.axvline(
    mean,
    color='#E57373',
    linestyle='--',
    linewidth=2,
    label='Mean'
)

plt.axvline(
    mean + std_dev,
    color='#A8CFA8',
    linestyle=':',
    linewidth=2,
    label='+1 Std Dev'
)

plt.axvline(
    mean - std_dev,
    color='#A8CFA8',
    linestyle=':',
    linewidth=2,
    label='-1 Std Dev'
)

plt.title('Binomial Distribution of COVID-19 Clinical Trials')
plt.xlabel('Number of Completed Trials')
plt.ylabel('Probability')
plt.legend()
plt.grid(axis='y', alpha=0.2)
plt.tight_layout()
plt.show()
# 10. Calculate probabilities

p_exactly_8 = binom.pmf(8, n, p)
p_at_least_5 = 1 - binom.cdf(4, n, p)
p_at_most_5 = binom.cdf(5, n, p)

print('P(X = 8):', p_exactly_8)
print('P(X >= 5):', p_at_least_5)
print('P(X <= 5):', p_at_most_5)