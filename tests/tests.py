import pandas as pd
import pytest
from pandicators.ma import simple_ma

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

