import numpy as np
import input_process as pro

U = np.load('../Training/eigen_space.npy')  # load eigenface
keys = np.load('../../db/user_keys.npy')  # load all users' keys in db

user = pro.process_input('input.png', (60, 90))  # preprocess user's image
Ukey = user @ U  # project it to eigenface space to get its key

# add this key to new_keys and store it in db
new_keys = []
for k in range(0, keys.shape[0]):
    new_keys.append(keys[k, :])
new_keys.append(Ukey)
new_keys = np.array(new_keys)

np.save('../../db/user_keys.npy', new_keys)
