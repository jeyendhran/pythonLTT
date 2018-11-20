import numpy as np
import matplotlib.pyplot as plt


#X = np.linspace(-1,1,256)
X = np.linspace(-np.pi,np.pi,256)
Y1 = np.sin(X)
#Y1 = np.sqrt(1 - X*X)
Y2 = np.cos(X)

plt.plot(X,Y1,color='red',linewidth=1,linestyle =':',label='Y1 plot')
plt.plot(X,Y2,color='maroon',linewidth=2,linestyle="-.",label="Y2 plot")
#plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi])
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
           [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$\pi/2$',r'$\pi$'],
           rotation =30) # to show pi symbol instead of 3.14

plt.yticks(range(-5,5))

#enhancement of the figure,spines color,position, ticks values
# plt.figure(figsize=(4,4),dpi=100)
# plt.xlim(X.min()*1.5)
# plt.ylim(Y1.min()*0.5)
#
ax = plt.gca()
ax.spines['right'].set_color(None)
ax.spines['top'].set_color(None)
ax.xaxis.set_ticks_position('top')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('right')
ax.spines['left'].set_position(('data',0))
#
# for label in ax.get_xticklabels()+ax.get_yticklabels():
#     label.set_fontsize(16)
#     label.set_bbox(dict(facecolor = 'red',edgecolor=None,alpha=0.1))
#
# #plt.xticks(range(0,5))
# plt.legend(loc='center')

# not working
#t = 2 * np.pi / 3
# plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
# plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
# plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',  xy=(t, np.sin(t)), xycoords='data', xytext=(+10, +30), textcoords='offset points', fontsize=16,  arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.show()
