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

def test_macd_invalid_dfObj():
    df = "Invalid_DF"
    with pytest.raises(TypeError):
        macd(df)

def test_macd_short_ema_value_errors():
    df = pd.DataFrame({"close": [0,1,2,3,4,5,6,7,8,9]})
    invalid_short_vals = [-1,8]
    test_long_ema = 7
    for val in invalid_short_vals:
        with pytest.raises(ValueError):
            macd(df,short_ema=val)

def test_macd_long_ema_value_errors():
    df = pd.DataFrame({"close": [0,1,2,3,4,5,6,7,8,9]})
    invalid_long_vals = [-1,7]
    test_short_ema = 8
    for val in invalid_long_vals:
        with pytest.raises(ValueError):
            macd(df,long_ema=val)

def test_macd_short_ema_type_error():
    df = pd.DataFrame({"close": [0,1,2,3,4,5,6,7,8,9]})
    with pytest.raises(TypeError):
        macd(df,short_ema="a")

def test_macd_long_ema_type_error():
    df = pd.DataFrame({"close": [0,1,2,3,4,5,6,7,8,9]})
    with pytest.raises(TypeError):
        macd(df,long_ema="a")