import tidypolars as tp
from tidypolars import col

def test_date():
    """Can do date operations"""
    df = tp.tibble(x = ['2021-01-01', '2021-10-01']).mutate(date = col('x').str.strptime(tp.Date))
    actual = (
        df
        .mutate(date_check = tp.as_date('x'),
                mday = tp.mday('date'),
                quarter = tp.quarter('date'),
                wday = tp.wday('date'),
                week = tp.week('date'),
                yday = tp.yday('date'),
                year = tp.year('date')
        )
    )
    expected = (
        tp.tibble(x = ['2021-01-01', '2021-10-01'])
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
    assert actual.equals(expected), "date operations failed"

def test_as_date_format():
    """Can pass fmt to as_date"""
    df = tp.tibble(date = ['12/31/2021'])
    out = df.mutate(date_parsed = tp.as_date(col('date'), format = '%m/%d/%Y'))
    assert out.pull().dtype == tp.Date, "as_date format failed"

def test_make_date():
    df = tp.tibble(date = ['2021-12-1']).mutate(date = tp.as_date('date'))
    out = df.mutate(date = tp.make_date(2021, 12, 1))
    assert df.pull('date').equals(out.pull('date')), "make_date failed"