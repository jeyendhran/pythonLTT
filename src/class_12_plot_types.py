import matplotlib.pyplot as plt
import numpy as np
#Scatter plots
# X = [12, -11, 13, 16, 15]
#
# Y = [7, -6, 8, 9, 10]
#
# plt.scatter(X,Y)

#Bar plots
# n = 12
# X = np.arange(n)
# Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
# Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
# plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
# plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
# for x, y in zip(X, Y1):
#     plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
# plt.ylim(-1.25, +1.25)

#Contour plots
# def f(x, y):
#     return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 -y ** 2)
#
# n = 256
# x = np.linspace(-3, 3, n)
# y = np.linspace(-3, 3, n)
# X, Y = np.meshgrid(x, y)
# plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='plasma')
# C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
#

plt.show()
