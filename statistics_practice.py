import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Random data generate karo jo Normal Distribution follow kare
data = np.random.normal(loc=0, scale=1, size=1000) 

# 2. Isse visualize karo (Seaborn use karke)
sns.histplot(data, kde=True)
plt.title("Gaussian Distribution")
plt.show()
