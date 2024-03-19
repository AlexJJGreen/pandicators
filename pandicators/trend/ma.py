import pandas as pd

def simple_ma(dataframe: pd.DataFrame, column: str, window_size: int) -> pd.Series:
    """
    Calculates the simple moving average for a specified column of a Pandas DataFrame.

    Parameters:
    - dataframe: <pandas.DataFrame> - Dataframe containing financial series
    - column: <str> - Name of column of dataframe for moving average calculation
    - window: <int> - number of periods of the moving average calculation

    Returns:
    - pandas.Series: A series containg the simple moving average of the specified column

    Raises:
    - ValueError: If window_size is less than 0 or greater than the length of series.
    - TypeError: If dataframe input is not an instance of pandas.Dataframe.
    """

    # errors
    if window_size <= 0:
        raise ValueError("window_size must be greater than 0")
    if window_size > len(dataframe):
        raise ValueError("window_size must be less than or equal to the length of the dataframe")
    if window_size is not int:
        raise TypeError("window_size must be an integer")
    if column not in dataframe.columns:
        raise ValueError(f"Column {column} could not be found in DataFrame")
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError(f"dataframe '{dataframe}' is not a valid instance of pandas.DataFrame")
    

    return dataframe[column].rolling(window=window_size).mean()