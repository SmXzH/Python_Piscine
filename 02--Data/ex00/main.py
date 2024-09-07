from load_csv import load

PATH = "../data/life_expectancy_years.csv"


def main():
    data = load(PATH)
    if data is not None:
        print(data)


if __name__ == '__main__':
    main()
