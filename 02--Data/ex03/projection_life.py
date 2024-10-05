from pandas import pandas as pd
from matplotlib import pyplot as plt


def projection_life(life_exp: pd.core.frame.DataFrame,
                    income: pd.core.frame.DataFrame):
    '''
    Display a scatter plot of the life expectancy and income of the year 1900.
    The x-axis should be the income
    and the y-axis should be the life expectancy.
    The x-axis should be in a logarithmic scale.
    The x-axis should have ticks at 300, 1000, and 10000
    with labels '300', '1k', and '10k'.
    The plot should have a title with the year.

    Parameters:

        life_exp (pandas.core.frame.DataFrame): The life expectancy dataset.
        income (pandas.core.frame.DataFrame): The income dataset.
    '''
    year = '1900'
    gnp1900 = income[year]
    life1900 = life_exp[year]
    print(gnp1900)
    print(life1900)

    plt.figure(figsize=(10, 6))
    plt.scatter(gnp1900, life1900)
    plt.xlabel('Gross domectic product')
    plt.xscale('log')
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.ylabel('Life expectancy in')
    plt.title(f'{year}')

    plt.show()
