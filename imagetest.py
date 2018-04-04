# -*- coding: utf-8 -*-
"""
opens two images in stereo mode 
"""
import sys
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

from PIL import Image
directory = "/home/lxfx/Desktop/Stereo/"

if len(sys.argv) == 2:
    photo_LDir = sys.argv[1]+"_L.jpg"
    photo_RDir = sys.argv[1]+"_R.jpg"
else:
    photo_LDir = sys.argv[1]
    photo_RDir = sys.argv[2]

border = "::::"
for i in range(len(photo_RDir)):
    border = border + ':'
print border
print ":", photo_RDir,":"
print ":", photo_LDir,":"
print border

photo_R = Image.open(directory+photo_RDir)
photo_L = Image.open(directory+photo_LDir)
photo_R = photo_R.rotate(270)
photo_L = photo_L.rotate(270)
array_R = np.asarray(photo_R)
array_L= np.asarray(photo_L)

# Interpret image data as row-major instead of col-major
# pg.setConfigOptions(imageAxisOrder='row-major')

pg.mkQApp()
win = pg.GraphicsLayoutWidget()
win.setWindowTitle('pyqtgraph example: Image Analysis')

# A plot area (ViewBox + axes) for displaying the image
p1 = win.addPlot()

# Item for displaying image data
img1 = pg.ImageItem()
p1.addItem(img1)

# A plot area (ViewBox + axes) for displaying the image
p2 = win.addPlot()

# Item for displaying image data
img2 = pg.ImageItem()
p2.addItem(img2)


win.resize(800, 800)
win.show()
img1.setImage(array_R)
img2.setImage(array_L)
# zoom to fit imageo
#p1.autoRange()  
#p2.autoRange()  
p1.setXLink(p2)
p1.setYLink(p2)

p1.showAxis('bottom', show=False)
p1.showAxis('left', show=False)
p2.showAxis('bottom', show=False)
p2.showAxis('left', show=False)


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
