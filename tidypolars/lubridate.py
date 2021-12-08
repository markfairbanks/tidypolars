import polars as pl
from .utils import _col_expr

__all__ = [
    "as_date",
    "as_datetime",
    "hour",
    "mday",
    "minute",
    "month",
    "quarter",
    "dt_round",
    "second",
    "wday",
    "week",
    "yday",
    "year"
]

def as_date(x, fmt = None):
    """
    Convert a string to a Date

    Parameters
    ----------
    x : Expr, Series
        Column to operate on
    fmt: str
        "yyyy-mm-dd"

    Examples
    --------
    >>> df = tp.Tibble(x = ['2021-01-01', '2021-10-01'])
    >>> df.mutate(date_x = tp.as_date(col('x')))
    """
    x = _col_expr(x)
    return x.str.strptime(pl.Date, fmt = fmt)

def as_datetime(x, fmt = None):
    """
    Convert a string to a Datetime

    Parameters
    ----------
    x : Expr, Series
        Column to operate on
    fmt: str
        "yyyy-mm-dd"

    Examples
    --------
    >>> df = tp.Tibble(x = ['2021-01-01', '2021-10-01'])
    >>> df.mutate(date_x = tp.as_datetime(col('x')))
    """
    x = _col_expr(x)
    return x.str.strptime(pl.Datetime, fmt = fmt)

def hour(x):
    """
    Extract the hour from a datetime

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(hour = tp.as_hour(col('x')))
    """
    x = _col_expr(x)
    return x.dt.hour()

def mday(x):
    """
    Extract the month day from a date from 1 to 31.

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(monthday = tp.mday(col('x')))
    """
    x = _col_expr(x)
    return x.dt.day()

def minute(x):
    """
    Extract the minute from a datetime

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(hour = tp.minute(col('x')))
    """
    x = _col_expr(x)
    return x.dt.minute()

def month(x):
    """
    Extract the month from a date

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(year = tp.month(col('x')))
    """
    x = _col_expr(x)
    return x.dt.month()

def quarter(x):
    """
    Extract the quarter from a date

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(quarter = tp.quarter(col('x')))
    """
    x = _col_expr(x)
    return (x.dt.month() // 4) + 1

def dt_round(x, rule, n):
    """
    Round the datetime

    Parameters
    ----------
    x : Expr, Series
        Column to operate on
    rule : str
        Units of the downscaling operation.
        Any of:
            - "month"
            - "week"
            - "day"
            - "hour"
            - "minute"
            - "second"
    n : int
        Number of units (e.g. 5 "day", 15 "minute".

    Examples
    --------
    >>> df.mutate(monthday = tp.mday(col('x')))
    """
    x = _col_expr(x)
    return x.dt.round()

def second(x):
    """
    Extract the second from a datetime

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(hour = tp.minute(col('x')))
    """
    x = _col_expr(x)
    return x.dt.second()

def wday(x):
    """
    Extract the weekday from a date from sunday = 1 to saturday = 7.

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(weekday = tp.wday(col('x')))
    """
    x = _col_expr(x)
    return x.dt.weekday() + 1

def week(x):
    """
    Extract the week from a date

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(week = tp.week(col('x')))
    """
    x = _col_expr(x)
    return x.dt.week()

def yday(x):
    """
    Extract the year day from a date from 1 to 366.

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(yearday = tp.yday(col('x')))
    """
    x = _col_expr(x)
    return x.dt.ordinal_day()

def year(x):
    """
    Extract the year from a date

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(year = tp.year(col('x')))
    """
    x = _col_expr(x)
    return x.dt.year()