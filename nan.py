import numpy as np
import matplotlib.pyplot as plt

data = np.random.random((10, 10))

plt.figure()
plt.imshow(data, origin='lower')   #(0,0)点在图片左下角
plt.colorbar()                     #画色标卡
plt.show()
