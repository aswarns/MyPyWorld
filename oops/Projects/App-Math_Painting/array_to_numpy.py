import numpy as np
from PIL import Image

data = np.zeros((5,4,3), dtype=np.uint8)
data[:] = [255,255,0]
print(data)

#making a red patch
data[0:3,0:2] = [255,220,233]
data[3:4,1:3] = [255,.255,233]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')