import numpy as np
import input_process as pro
from numpy import linalg as LA
import matplotlib.pyplot as plt

U = np.load('../Training/eigen_space.npy')  # load eigenface
keys = np.load('../../db/user_keys.npy')  # load all users' keys in db

test = pro.process_input('input.png', (60, 90))  # preprocess test image
Tkey = test @ U  # project test image to eigenface space to get its key
output = []
for k in range(0, keys.shape[0]):
    output.append(LA.norm(Tkey - keys[k, :]))
    if LA.norm(Tkey - keys[k, :]) < 7.5:  # if its key matches any other image's key in db
        print(True)  # this face is recognized
        pass

x = np.arange(keys.shape[0])
plt.scatter(x, output)
plt.plot(x, output)
plt.show()

print(False)
