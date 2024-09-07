from load_csv import load
from aff_pop import aff_pop


PATH = "../data/population_total.csv"


def main():
    data = load(PATH)
    if data is not None:
        print(data)
    aff_pop(data, 'United Arab Emirates', 'France')


if __name__ == '__main__':
    main()
