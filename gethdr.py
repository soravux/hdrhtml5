import sys
import json

import numpy as np
import scipy.ndimage
from hdrio import imread

# Usage : gethdr.py source dest

image = imread(sys.argv[1])
imresized = scipy.ndimage.interpolation.zoom(image, (580./image.shape[0], 580/image.shape[1], 1), order=1)
alpha = np.zeros(imresized.shape[0:2]) + 255.
imresizeda = np.dstack((imresized, alpha))
out = imresizeda
with open(sys.argv[2], 'w') as fhdl:
    fhdl.write("var targetData = ")
    json.dump(out.flatten().tolist(), fhdl)
    fhdl.write(";")
