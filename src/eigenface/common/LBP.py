import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def get_texture(input_mat):
    """
    Use LBP (local binary patterns) to extract the texture of an image
    :param input_mat:
    :return:
    """
    row, col = input_mat.shape
    output = np.zeros((row, col))
    for i in range(1, row - 1):
        for j in range(1, col - 1):
            output[i, j] = int(get_bin(input_mat, i, j), 2)
    return output


def get_bin(matrix, i, j):
    bina = "0b"
    cur = matrix[i, j]

    for k in range(j-1, j+2):
        bina = bina + str("1" if matrix[i-1, k] > cur else "0")

    bina = bina + str("1" if matrix[i, j+1] > cur else "0")

    for k in range(j+1, j-2, -1):
        bina = bina + str("1" if matrix[i+1, k] > cur else "0")

    bina = bina + str("1" if matrix[i, j-1] > cur else "0")

    return bina


image = cv.imread('../Training/Data/Cheng2.jpg', 0)  # read gray-scale
image = cv.resize(image, (150, 200))  # resize to standard resolution
image = np.array(image)  # transform to numpy matrix
image = get_texture(image)  # extract texture
plt.imshow(image)
plt.show()
