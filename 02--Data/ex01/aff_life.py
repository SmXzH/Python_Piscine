from matplotlib import pyplot as plt
from pandas import pandas


def aff_life(data: pandas.core.frame.DataFrame, country: str):
    '''
    Display a line plot of the life expectancy of the given country.
    If the country is not found in the dataset, print "Error: {country}
    not found in dataset."

    Parameters:
        data (pandas.core.frame.DataFrame): The dataset.
        country (str): The country to display the life expectancy of.
    '''
    if data is None:
        print("Failed to load the dataset.")
        return

    new_df = (data[data['country'] == country])
    if new_df.empty:
        print(f"Error: {country} not found in dataset.")
        return
    new_df = new_df.drop(columns=['country'])
    new_df = new_df.T
    new_df.plot(kind='line', title=f"Life expectancy in {country}",
                legend=True, grid=True, color='blue', linewidth=2.5)
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title(f'{country} Life expectancy Projection', fontsize=10)
    plt.show()
