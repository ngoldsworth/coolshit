import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Data Analysis, question 5
amounts2=[0.0397,0.04256,0.04827,0.03668,0.04483,0.03276]
hpm2=np.array([91100,87400,89876,95355,98952,88405])
hpm1=np.array([36450.,38740.,35620.,44780.,46800.,35290.])
hpm3=np.array([21610,15490,23310,21390,30220,1.820e3])
# plt.show()
# tup = linregress(part1amounts, part1hpm)
# print(tup)
print((hpm1+hpm3)/hpm2)

moles2=np.array([0.0397,0.04256,0.04827,0.03668,0.04483,0.03276])
heats2=np.array([3620,3720,4340,3498,4440,2.90e3])
plt.scatter(moles2, heats2)
m, b, r, p, err = linregress(moles2, heats2)
x = np.array([.03, .05])
y = m*x + b
plt.plot(x, y)
