from pandas import pandas as pd
from matplotlib import pyplot as plt


def parsing_population(pop_str: str):
    '''
    Parse the population string and return the population as a float.
    The population string can end with 'M' for million or 'k' for thousand.
    If the population string ends with 'M', multiply the number by 1e6.
    If the population string ends with 'k', multiply the number by 1e3.
    If the population string does not end with 'M' or 'k',
        return the number as a float.

    Parameters:
        pop_str (str): The population string.

    Returns:
        float: The population as a float.
    '''
    if pop_str.endswith('M'):
        return float(pop_str[:-1]) * 1e6
    elif pop_str.endswith('k'):
        return float(pop_str[:-1]) * 1e3
    else:
        return float(pop_str)


def aff_pop(data: pd.core.frame.DataFrame, country1: str, country2: str):
    '''
    Display a line plot of the population of the given countries.
    If a country is not found in the dataset, print "Error: {country}
        not found in dataset."

    Parameters:
        data (pandas.core.frame.DataFrame): The dataset.
        country1 (str): The first country to display the population of.
        country2 (str): The second country to display the population of.
    '''
    if data is None:
        print("Failed to load the dataset.")
        return

    df1 = data[data['country'] == country1].iloc[:, 1:]
    df2 = data[data['country'] == country2].iloc[:, 1:]

    if df1.empty:
        print(f"Error: {country1} not found in dataset.")
        return
    if df2.empty:
        print(f"Error: {country2} not found in dataset.")
        return

    pop_country1 = df1.values.flatten()
    pop_country2 = df2.values.flatten()
    years = data.columns[1:].astype(int)

    pop_country1 = [parsing_population(pop) for pop in pop_country1]
    pop_country2 = [parsing_population(pop) for pop in pop_country2]

    plt.plot(years, pop_country1, label=country1, color='green')
    plt.plot(years, pop_country2, label=country2)

    plt.xlabel('Year')
    plt.xticks(range(1800, 2051, 40))
    plt.xlim(1800, 2040)
    plt.ylabel('Population')
    plt.title('Population Projection')
    plt.legend()
    plt.show()
