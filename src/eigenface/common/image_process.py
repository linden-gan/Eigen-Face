import cv2 as cv
import numpy as np
from src.eigenface.common import LBP
import matplotlib.pyplot as plt


def process_img(file_name, dim):
    """
    Initial parse here
    :param dim: desired dimension of new image in pixels
    :param file_name: image name in a directory
    :return: an array (flatten) of parsed, gray-scale image
    """
    image = cv.imread(file_name, 0)  # read gray-scale
    image = cv.resize(image, dim)  # resize to standard resolution
    image = np.array(image)  # transform to numpy matrix
    #image = LBP.get_texture(image)  # extract texture
    image = image.flatten()  # transform to an array

    model = cv.imread('src/eigenface/common/Model_Medium.png', 0)  # read gray-scale
    model = cv.resize(model, dim)  # resize to standard resolution
    model = np.array(model).flatten()  # transform to an array

    # scoop face from image according to model
    for k in range(0, len(model)):
        if model[k] < 2:
            image[k] = 0

    return image / 255
















