import numpy as np


def ft_zoom(data: np.array) -> np.array:
    '''
    The function takes a 3D numpy array and returns a 3D numpy array of the image after zooming.

    Parameters:
        data (np.array): The 3D numpy array of the image.
    '''
    res = data[100:500, 450:850, 0:3]
    print(f"shape after slicing is {res.shape}")
    return res