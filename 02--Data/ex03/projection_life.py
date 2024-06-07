from pandas import pandas as pd
from matplotlib import pyplot as plt

def projection_life(life_exp : pd.core.frame.DataFrame, income : pd.core.frame.DataFrame):
    year = '1900'
    gnp1900 = income[year]
    life1900 = life_exp[year]
    print(gnp1900)
    print(life1900)

    plt.figure(figsize=(10, 6))
    plt.scatter(gnp1900, life1900)
    plt.xlabel(f'Gross domectic product')
    plt.xscale('log')
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.ylabel(f'Life expectancy in')
    plt.title(f'{year}')

    plt.show()
