from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    '''
    The function takes a path to an image and returns a
    3D numpy array of the image.

    Parameters:
        path (str): The path to the image.
    '''
    img = Image.open(path)

    print(f"The shape of image is: {img.format}")
    img_conv = img.convert("RGB")
    img_arr = np.array(img_conv)
    print(f"The shape of the image is: {img_arr.shape}")
    print(img_arr)

    return img_arr
