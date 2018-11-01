import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#fig = plt.figure(figsize=(8,6))
# Draw multiple plots in one plot view

# fig.add_subplot(331).hist(np.random.randn(100),bins =20,color='k',alpha=0.4)
# fig.add_subplot(333).scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))
# fig.add_subplot(3,3,4)
# fig.add_subplot(3,3,8)

#Sharing x and y axes
# fig,axes = plt.subplots(2,2,sharex=False,sharey=False   )
# for i in range(2):
#     for j in range(2):
#         axes[i,j].hist(np.random.randn(500),bins=50,color='b',alpha=0.4)
# adjust the vertical and horizontal space between subplots
#plt.subplots_adjust(wspace=0,hspace=0.1)

# To show shapes in plots
# ax = fig.add_subplot(1, 1, 1)
# rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
# circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.3)
# pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]], color='g', alpha=0.5)
# ax.add_patch(rect)
# ax.add_patch(circ)
# ax.add_patch(pgon)

# for series index is x axis and values is y axis
# stocks = pd.Series([12,10,8,6,0],
#                    index= [1,2,3,4,5])
# stocks.plot()

# For dataframes index is x axis and each dict is taken as diff curves
dataFrame = pd.DataFrame({"qty":[10,23,45,25,24],
                          "fg":[2,3,4,5,6],
                          "st":["tn","ap","kr","ka","mb"]},
                          index=[97,98,101,100,88])

dataFrame.plot()

#To save the plot in png or pdf format
#plt.savefig("myplt.pdf")

plt.show()
