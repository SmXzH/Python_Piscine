from load_csv import load


def main():
    PATH = "../data/life_expectancy_years.csv"
    data = load(PATH)
    if data is not None:
        print(data)


if __name__ == '__main__':
    main()
