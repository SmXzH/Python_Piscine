from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    '''
    The function takes a path to an image and returns
    a 3D numpy array of the image.

    Parameters:
        path (str): The path to the image.
    '''
    img_arr = None
    try:
        img = Image.open(path)
        if img.format is not None and img.format.lower() in ['jpeg', 'jpg']:
            print(f"The format of image is: {img.format}")
            img_conv = img.convert('RGB')
            img_arr = np.array(img_conv)
            print(f"The shape of the image is: {img_arr.shape}")
            # print(img_arr)
        else:
            print("Error: Unsupported image format")
    except Exception as e:
        print(f"Error: {e}")

    return img_arr
