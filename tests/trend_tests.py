import pandas as pd
import pytest
from pandicators.trend.ma import simple_ma



def test_simple_ma():
    df = pd.DataFrame({"values": [1,2,3,4,5]})

    # calculate ma window size 2
    result = simple_ma(df, "values", 2)
    expected = pd.Series([None, 1.5,2.5,3.5,4.5], name="values")
    pd.testing.assert_series_equal(result, expected)

def test_simple_ma_invalid_column():
    df = pd.DataFrame({"values": [1,2,3]})
    with pytest.raises(ValueError):
        simple_ma(df,"invalid_column",2)

def test_simple_ma_invalid_window_size():
    df = pd.DataFrame({"values": [1,2,3]})
    with pytest.raises(ValueError):
        simple_ma(df,"values", -1)



from pandicators.trend.macd import macd

def test_macd():
    df = pd.DataFrame({"values": [1,2,3,4,5,6,7,8,9]})

    # calculate values short_ema 2, long_ema 4, signal 3
    result = macd(df,column="values", short_ema=2,long_ema=4,signal=3,concat=False)
    expected = [pd.Series([0.000000,
                           0.266667,
                           0.515556,
                           0.694519,
                           0.811773,
                           0.885418,
                           0.930702,
                           0.958238,
                           0.974882],
                           name="MACD"),
                pd.Series([0.000000,
                           0.133333,
                           0.324444,
                           0.509481,
                           0.660627,
                           0.773022,
                           0.851862,
                           0.905050,
                           0.939966],
                           name="MACD_Signal")]
    for i,df in enumerate(expected):
        pd.testing.assert_series_equal(result[i],df)