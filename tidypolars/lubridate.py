import polars as pl
from .utils import _col_expr

__all__ = [
    "dt_as_date",
    "dt_as_datetime",
    "dt_hour",
    "dt_mday",
    "dt_minute",
    "dt_month",
    "dt_quarter",
    "dt_round",
    "dt_second",
    "dt_wday",
    "dt_week",
    "dt_yday",
    "dt_year"
]

def dt_as_date(x, fmt = None):
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
    >>> df.mutate(date_x = tp.dt_as_date(col('x')))
    """
    x = _col_expr(x)
    return x.str.strptime(pl.Date)

def dt_as_datetime(x, fmt = None):
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
    >>> df.mutate(date_x = tp.dt_as_datetime(col('x')))
    """
    x = _col_expr(x)
    return x.str.strptime(pl.Datetime)

def dt_hour(x):
    """
    Extract the hour from a datetime

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(hour = tp.dt_hour(col('x')))
    """
    x = _col_expr(x)
    return x.dt.hour()

def dt_mday(x):
    """
    Extract the month day from a date from 1 to 31.

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(monthday = tp.dt_mday(col('x')))
    """
    x = _col_expr(x)
    return x.dt.day()

def dt_minute(x):
    """
    Extract the minute from a datetime

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(hour = tp.dt_minute(col('x')))
    """
    x = _col_expr(x)
    return x.dt.minute()

def dt_month(x):
    """
    Extract the month from a date

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(year = tp.dt_month(col('x')))
    """
    x = _col_expr(x)
    return x.dt.month()

def dt_quarter(x):
    """
    Extract the quarter from a date

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(quarter = tp.dt_quarter(col('x')))
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
    >>> df.mutate(monthday = tp.dt_mday(col('x')))
    """
    x = _col_expr(x)
    return x.dt.round()

def dt_second(x):
    """
    Extract the second from a datetime

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(hour = tp.dt_minute(col('x')))
    """
    x = _col_expr(x)
    return x.dt.second()

def dt_wday(x):
    """
    Extract the weekday from a date from sunday = 1 to saturday = 7.

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(weekday = tp.dt_wday(col('x')))
    """
    x = _col_expr(x)
    return x.dt.weekday() + 1

def dt_week(x):
    """
    Extract the week from a date

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(week = tp.dt_week(col('x')))
    """
    x = _col_expr(x)
    return x.dt.week()

def dt_yday(x):
    """
    Extract the year day from a date from 1 to 366.

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(yearday = tp.dt_yday(col('x')))
    """
    x = _col_expr(x)
    return x.dt.ordinal_day()

def dt_year(x):
    """
    Extract the year from a date

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(year = tp.dt_year(col('x')))
    """
    x = _col_expr(x)
    return x.dt.year()