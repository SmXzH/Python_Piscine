from load_image import ft_load
from zoom import ft_zoom
import matplotlib.pyplot as plt
from ft_transpose import ft_transpose


def main():
    res = ft_load("/Users/sam/Desktop/Python Picine/01--Array/ex03/pic/"
                  "animal.jpeg")
    res = ft_zoom(res)
    res = ft_transpose(res)
    plt.imshow(res)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.show()


if __name__ == "__main__":
    main()
