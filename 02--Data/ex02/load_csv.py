from pandas import read_csv


def load(path):
    '''
    Load a CSV file from the given path.
    If the file is loaded successfully, print "Data loaded
        successfully" and return the data.
    If the file is not loaded successfully, print "Error: {error message}"
        and return None.

    Parameters:
        path (str): The path to the CSV file.
    '''
    try:
        data = read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None
