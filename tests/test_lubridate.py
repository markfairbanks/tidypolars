import tidypolars as tp
from tidypolars import col
import math

def test_date():
    """Can do date operations"""
    df = tp.Tibble(x = ['2021-01-01', '2021-10-01']).mutate(date = col('x').str.strptime(tp.Date))
    actual = (
        df
        .mutate(date_check = tp.dt_as_date('x'),
                mday = tp.dt_mday('date'),
                quarter = tp.dt_quarter('date'),
                wday = tp.dt_wday('date'),
                week = tp.dt_week('date'),
                yday = tp.dt_yday('date'),
                year = tp.dt_year('date')
        )
    )
    expected = (
        tp.Tibble(x = ['2021-01-01', '2021-10-01'])
        .mutate(date = col('x').str.strptime(tp.Date))
        .mutate(date_check = col('date'),
                mday = col('date').dt.day(),
                quarter = tp.Series([1, 3]),
                wday = col('date').dt.weekday() + 1,
                week = col('date').dt.week(),
                yday = col('date').dt.ordinal_day(),
                year = col('date').dt.year()
                )
    )
    assert actual.frame_equal(expected), "date operations failed"