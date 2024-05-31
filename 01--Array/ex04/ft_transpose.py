import numpy as np


def ft_transpose(res: np.array) -> np.array:
    '''
    The function takes a 3D numpy array and returns a 3D numpy array of
    the image after transposing it.

    Parameters:
        data (np.array): The 3D numpy array of the image.
    '''
    h, w, c = res.shape
    trancpose_data = np.zeros((w, h, c), dtype=res.dtype)
    for i in range(h):
        for j in range(w):
            trancpose_data[j, i] = res[i, j]

    return trancpose_data
