import polars as pl
import functools as ft
from .utils import (
    _as_list,
    _col_expr,
    _col_exprs,
    _kwargs_as_exprs,
    _mutate_cols,
    _uses_by
)
from .stringr import str_c
import copy
from .reexports import *
from .tidyselect import everything
from operator import not_

from .tibble import desc, DescCol

__all__ = [
    "arrange",
    "filter",
    "mutate"
]
from .pipe import dfpipe

@dfpipe
def arrange(df, *args):
    """
    Arrange/sort rows

    Parameters
    ----------
    *args : str
        Columns to sort by

    Examples
    --------
    >>> df = tp.Tibble({'x': ['a', 'a', 'b'], 'y': range(3)})
    >>> # Arrange in ascending order
    >>> df.arrange('x', 'y')
    ...
    >>> # Arrange some columns descending
    >>> df.arrange(tp.desc('x'), 'y')
    """
    exprs = _as_list(args)
    desc = [True if isinstance(expr, DescCol) else False for expr in exprs]
    return df.sort(exprs, reverse = desc)

@dfpipe
def filter(df, *args, by = None):
    """
    Filter rows on one or more conditions

    Parameters
    ----------
    *args : Expr
        Conditions to filter by
    by : str, list
        Columns to group by

    Examples
    --------
    >>> df = tp.Tibble({'a': range(3), 'b': ['a', 'a', 'b']})
    >>> df.filter(col('a') < 2, col('b') == 'a')
    >>> df.filter((col('a') < 2) & (col('b') == 'a'))
    >>> df.filter(col('a') <= tp.mean(col('a')), by = 'b')
    """
    args = _as_list(args)
    exprs = ft.reduce(lambda a, b: a & b, args)

    if _uses_by(by):
        out = df.groupby(by).apply(lambda x: x.filter(exprs))
    else:
        out = df.filter(exprs)
    
    return out

@dfpipe
def mutate(df, *args, by = None, **kwargs):
    """
    Add or modify columns

    Parameters
    ----------
    *args : Expr
        Column expressions to add or modify
    by : str, list
        Columns to group by
    **kwargs : Expr
        Column expressions to add or modify

    Examples
    --------
    >>> df = tp.Tibble({'a': range(3), 'b': range(3), c = ['a', 'a', 'b']})
    >>> df.mutate(double_a = col('a') * 2,
    ...           a_plus_b = col('a') + col('b'))
    >>> df.mutate(row_num = row_number(), by = 'c')
    """
    exprs = _as_list(args) + _kwargs_as_exprs(kwargs)

    if _uses_by(by):
        out = df.groupby(by).apply(lambda x: _mutate_cols(x, exprs))
    else:
        out = _mutate_cols(df, exprs)
        
    return out