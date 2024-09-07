from load_csv import load
from aff_pop import aff_pop


def main():
    PATH = "../data/population_total.csv"
    data = load(PATH)
    if data is not None:
        print(data)
    aff_pop(data, 'United Arab Emirates', 'France')


if __name__ == '__main__':
    main()
