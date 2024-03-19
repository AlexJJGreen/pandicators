import pandas as pd
from typing import List

def macd(dataframe: pd.DataFrame, column: str = "close", short_ema: int = 12, long_ema: int = 26, signal: int = 9, concat: bool = True) -> List[pd.Series] | pd.DataFrame:
    """
    Generates MACD and Signal line indicators for a Panada Dataframe.
    - By default, these are concatenated to the given DataFrame.
    - Setting contcat to False will return a list of the individual pd.Series

    Parameters:
    - dataframe: <pandas.DataFrame> containing the stock price.
    - column: <str> column name of the closing price series.
    - short_ema: <int> (default = 12) periods for the short exponential moving average. short_ema must be < long_ema
    - long_ema: <int> (default = 26) periods for the long exponential moving average. long_ema must be > short_ema
    - signal: <int> (default = 9) period for the MACD signal line.
    """
    # error handling
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError(f"dataframe '{dataframe}' is not a valid instance of pandas.DataFrame")
    if not isinstance(short_ema, int):
        raise TypeError("short_ema must be an instance if int")
    if not isinstance(long_ema, int):
        raise TypeError("long_ema must be an instance of type int")
    if not isinstance(concat, bool):
        raise TypeError("concat must be a True or False boolean value")
    if column not in dataframe.columns:
        raise ValueError(f"Column '{column}' could not be found in {dataframe}")
    if short_ema < 0:
        raise ValueError("short_ema must be a positive integer")
    if long_ema < 0:
        raise ValueError("long_ema must be a positive integer")
    if signal < 0:
        raise ValueError("signal must be a positive integer")
    if short_ema > len(dataframe):
        raise ValueError(f"short_ema must be less than the length of {dataframe}")
    if long_ema > len(dataframe):
        raise ValueError(f"long_ema must be less than the length of {dataframe}")
    if signal > len(dataframe):
        raise ValueError(f"signal must be less than the length of {dataframe}")
    if short_ema > long_ema:
        raise ValueError(f"short_ema must be less than long_ema")
    
    sema = dataframe[column].ewm(span=short_ema, adjust=False).mean()
    lema = dataframe[column].ewm(span=long_ema,adjust=False).mean()
    macd_series = pd.Series(data=(sema - lema), name="MACD")
    signal_series = pd.Series(data=(macd_series.ewm(span=signal, adjust=False).mean()), name="MACD_Signal")

    if concat:
        dataframe['MACD'] = macd_series
        dataframe["MACD_Signal"] = signal_series
        return dataframe
    else:
        return [macd_series,signal_series]

