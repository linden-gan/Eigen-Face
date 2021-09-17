import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
from pathlib import Path

from src.eigenface.common import image_process as pro

width = 60  # the standard width, in pixels, of images
height = 90  # the standard height, in pixels, of images
pixel_num = width * height
face_dim = (width, height)

# parse and store all training images into a Data matrix
Data = []
ave = np.zeros(pixel_num)
folder = Path('Data')
for file in folder.iterdir():
    if file.is_file():
        image_vec = pro.process_img('Data/' + file.name, face_dim)
        ave = ave + image_vec
        Data.append(image_vec)

face_num = len(Data)
ave = ave / face_num  # compute the average image

Data = np.array(Data)  # transform Data to a matrix (nd-array)
for k in range(0, face_num):  # normalize each image by subtracting average image
    Data[k, :] = Data[k, :] - ave

Data = np.transpose(Data)  # we just prefer its transpose, where images are stored in columns

# Do PCA analysis on Data, extract first 20 columns of U as dominant eigenfaces
U, S, V = LA.svd(Data, full_matrices=False)
U = U[:, 0:20]

# dump training model result to .npy files
np.save('eigen_space.npy', U)
np.save('ave_face.npy', ave)

# Test
Keys = np.transpose(Data) @ U
Test = pro.process_img('Data/Roven1.png', face_dim)
Test = Test - ave
TKey = Test @ U
output = []
for k in range(0, face_num):
    output.append(LA.norm(TKey - Keys[k, :]))

x = np.arange(face_num)
plt.scatter(x, output)
plt.plot(x, output)
plt.show()
