import cv2 as cv
import numpy as np


def process_input(file_name, dim):
    """
    Initial parse here
    :param dim: desired dimension of new image in pixels
    :param file_name: image name in a directory
    :return: an array (flatten) of parsed, gray-scale image
    """
    image = cv.imread(file_name, 0)  # read gray-scale
    image = cv.resize(image, dim)  # resize to standard resolution
    image = np.array(image).flatten()  # transform to an array

    model = cv.imread('../Training/Model_Medium.png', 0)  # read gray-scale
    model = cv.resize(model, dim)  # resize to standard resolution
    model = np.array(model).flatten()  # transform to an array

    # scoop face from image according to model
    for k in range(0, len(model)):
        if model[k] < 5:
            image[k] = 0

    image = image / 255
    ave = np.load('../Training/ave_face.npy')
    return image - ave
