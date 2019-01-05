import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# income = np.random.normal(27000, 15000, 10000)

# print(np.mean(income))


# ages = np.random.randint(18, high=90, size=500)

# print(ages)

# print(stats.mode(ages))

incomes = np.random.normal(100.0, 20.0, 10000)

plt.hist(incomes, 50)

print(np.median(incomes))

print(np.mean(incomes))