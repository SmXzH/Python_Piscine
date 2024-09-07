from load_csv import load
from projection_life import projection_life


def main():
    PATH = "../data/life_expectancy_years.csv"
    PATH_2 = "../data/income_per_person_gdppercapita.csv"
    data = load(PATH)
    data2 = load(PATH_2)
    # if data is not None:
    #     print(data)
    projection_life(data, data2)


if __name__ == '__main__':
    main()
