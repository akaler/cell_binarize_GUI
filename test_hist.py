import skimage.color
import skimage.io
import skimage.viewer
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 


if __name__ == "__main__":

    im_phase = skimage.io.imread("{}.png".format(1))
    hist_phase, bins_phase = skimage.exposure.histogram(im_phase)


    # Use matplotlib to make a pretty plot of histogram data

    fig, ax = plt.subplots()
    
    ax.set_xlabel('pixel value')

    ax.set_ylabel('count')

    ratio = 0.001

    xleft, xright = ax.get_xlim()
    ybottom, ytop = ax.get_ylim()
    _ = ax.fill_between(bins_phase, hist_phase, alpha=0.75)
    plt.show()


    """
    im_phase = skimage.io.imread("{}.png".format(0))
    hist_phase, bins_phase = skimage.exposure.histogram(im_phase)


    # Use matplotlib to make a pretty plot of histogram data

    fig, ax = plt.subplots(1, 1)

    ax.set_xlabel('pixel value')

    ax.set_ylabel('count')

    #_ = ax.fill_between(bins_phase, hist_phase, alpha=0.75)
    #fig.show()
    #_ = ax.plot([300, 300], [0, 35000])
    """
