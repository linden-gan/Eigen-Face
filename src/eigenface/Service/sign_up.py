import numpy as np

from src.eigenface.common import image_process as pro


def sign_up():
    U = np.load('src/eigenface/Training/eigen_space.npy')  # load eigenface
    keys = np.load('src/db/user_keys.npy')  # load all users' keys in db
    ave = np.load('src/eigenface/Training/ave_face.npy')  # load average face

    user = pro.process_img('src/eigenface/Service/input.png', (60, 90))  # preprocess user image
    user = user - ave
    Ukey = user @ U  # project it to eigenface space to get its key

    # add this key to new_keys and store it in db
    new_keys = []
    for k in range(0, keys.shape[0]):
        new_keys.append(keys[k, :])
    new_keys.append(Ukey)
    new_keys = np.array(new_keys)

    np.save('src/db/user_keys.npy', new_keys)









