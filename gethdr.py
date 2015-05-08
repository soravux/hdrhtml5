from hdrio import imread
import json
import numpy as np
import scipy.ndimage

image = imread('envmap.exr')
imresized = scipy.ndimage.interpolation.zoom(image, (0.15, 0.15, 1), order=1)
alpha = np.ones(imresized.shape[0:2])
imresizeda = np.dstack((imresized, alpha))
out = imresizeda
print(out[:3,:3,:])
print(out.flatten()[:20])
with open('targetData.js', 'w') as fhdl:
    fhdl.write("var targetData = ")
    json.dump(out.flatten().tolist(), fhdl)
    fhdl.write(";")