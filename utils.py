import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 


def plot_track(t1,l1=None,t2=None,l2=None, title=None):
    """
    t1 -> track 1
    l1 -> label 1

    """
    
    
    fig=plt.figure(figsize=(60,20))
    ax0 = fig.add_subplot(2, 2, 1, projection='3d')

    # tennis court
    xx, yy = np.meshgrid(range(-5,6), range(-12,13))
    zz = xx*0
    ax0.plot_surface(xx, yy, zz, color='orange',alpha=0.3)

    # net
    xx, zz = np.meshgrid(range(-5,6), range(0,2))
    yy = xx*0
    ax0.plot_surface(xx, yy, zz, color='black',alpha=0.2)

    if l1 is None:
        l1 = 'Track point'
    # track1
    ax0.scatter(t1[:,1],t1[:,2],t1[:,3], s = 40, c = 'blue', alpha = 1, label = l1)

    if t2 is not None:
        if l2 is None:
            l2 = 'Track point 2'
        # track2
        ax0.scatter(t2[:,1],t2[:,2],t2[:,3], s = 40, color='yellow', edgecolor='blue', alpha = 1, label = l2)

    ax0.view_init(azim=30,elev=30)
    ax0.set_xlabel('x',fontsize=16)
    ax0.set_ylabel('y',fontsize=16)
    ax0.set_zlabel('z',fontsize=16)

    ax0.set_xlim([-6.5,6.5])
    ax0.set_ylim([-15,15])
    ax0.set_zlim([0,6])
    ax0.legend(fontsize = 20)
    
    if title is not None:
        ax0.set_title(title,fontsize=22)