from load_csv import load
from aff_life import aff_life


def main():
    PATH = "../data/life_expectancy_years.csv"
    data = load(PATH)
    if data is not None:
        print(data)
    aff_life(data, 'United Arab Emirates')


if __name__ == '__main__':
    main()
