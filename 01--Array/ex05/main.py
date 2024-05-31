from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
from matplotlib import pyplot as plt


def main():
    res = ft_load("/Users/sam/Desktop/Python Picine/01--Array/ex05/pic/"
                  "landscape.jpg")
    f, axarr = plt.subplots(3, 2)
    axarr[0, 0].imshow(res)
    axarr[0, 1].imshow(ft_invert(res))
    axarr[1, 0].imshow(ft_red(res))
    axarr[1, 1].imshow(ft_green(res))
    axarr[2, 0].imshow(ft_blue(res))
    axarr[2, 1].imshow(ft_grey(res))
    plt.show()


if __name__ == "__main__":
    main()
