from load_csv import load
from projection_life import projection_life


PATH = "/Users/sam/Desktop/Python_Piscine/02--Data/data/life_expectancy_years.csv"
PATH_2 = "/Users/sam/Desktop/Python_Piscine/02--Data/data/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"


def main():
    data = load(PATH)
    data2 = load(PATH_2)
    # if data is not None:
    #     print(data)
    projection_life(data, data2)


if __name__ == '__main__':
    main()
