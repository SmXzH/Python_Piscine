import numpy as np


def ft_invert(array) -> np.array:
    '''
    The function takes a 3D numpy array and returns a
    3D numpy array of the image after inverting.

    Parameters:
        array (np.array): The 3D numpy array of the image.
    '''
    return 255 - array


def ft_red(array) -> np.array:
    '''
    The function takes a 3D numpy array and returns a
    3D numpy array of the image after extracting the red channel.

    Parameters:
        array (np.array): The 3D numpy array of the image.
    '''
    result = np.zeros_like(array)
    result[:, :, 0] = array[:, :, 0]
    return result


def ft_green(array) -> np.array:
    '''
    The function takes a 3D numpy array and returns a
    3D numpy array of the image after extracting the green channel.

    Parameters:
        array (np.array): The 3D numpy array of the image.
    '''
    result = np.zeros_like(array)
    result[:, :, 1] = array[:, :, 1]
    return result


def ft_blue(array) -> np.array:
    '''
    The function takes a 3D numpy array and returns a
    3D numpy array of the image after extracting the blue channel.

    Parameters:
        array (np.array): The 3D numpy array of the image.
    '''
    result = np.zeros_like(array)
    result[:, :, 2] = array[:, :, 2]
    return result


def ft_grey(array) -> np.array:
    '''
    The function takes a 3D numpy array and returns a
    3D numpy array of the image after converting it to grey scale.

    Parameters:
        array (np.array): The 3D numpy array of the image.
    '''
    red = array[:, :, 0]
    green = array[:, :, 1]
    blue = array[:, :, 2]

    grey = (red / 3 + green / 3 + blue / 3).astype(np.uint8)
    grey = np.stack((grey, grey, grey), axis=2)

    return grey
