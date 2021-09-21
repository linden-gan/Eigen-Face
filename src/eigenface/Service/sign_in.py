import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

from src.eigenface.common import image_process as pro


def sign_in():
    U = np.load('src/eigenface/Training/eigen_space.npy')  # load eigenface
    keys = np.load('src/db/user_keys.npy')  # load all users' keys in db
    ave = np.load('src/eigenface/Training/ave_face.npy')  # load average face

    user = pro.process_img('src/eigenface/Service/input.png', (60, 90))  # preprocess user image
    user = user - ave
    Ukey = user @ U  # project test image to eigenface space to get its key
    # output = []
    for k in range(0, keys.shape[0]):
        # output.append(LA.norm(Ukey - keys[k, :]))
        print(LA.norm(Ukey - keys[k, :]))
        if LA.norm(Ukey - keys[k, :]) < 6.0:  # if its key matches any other image's key in db
            return True

    # print(output)
    # x = np.arange(keys.shape[0])
    # plt.scatter(x, output)
    # plt.plot(x, output)
    # plt.show()

    return False

















