from tidypolars import col
import polars as pl
import functools as ft
from .utils import _col_expr
from .funs import is_not

__all__ = [
    "str_detect", 
    "str_to_upper", 
    "str_to_lower"
    ]

def str_detect(string : str, pattern : str, negate: bool = False):
    """
    Detect the presence or absence of a pattern in a string

    Parameters
    ----------
    string : str
        Input series to operate on
    pattern : str
        Pattern to look for
    negate : bool
        If True, return non-matching elements

    Examples
    --------
    >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    >>> df.mutate(detect_single = str_detect('name', ['a']))
    >>> df.mutate(detect_multiple = str_detect('name', ['a', 'e']))
    """
    if isinstance(pattern, str):
        [pattern]
    
    string = _col_expr(string)

    exprs = (string.str.contains(p) for p in pattern)
    exprs = ft.reduce(lambda a, b : a & b, exprs)
    if negate:
        exprs = exprs.is_not()
    
    return exprs

def str_to_upper(string : str):
    """
    Convert case of a string

    Parameters
    ----------
    string : str
        Convert case of this string

    Examples
    --------
    >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    >>> df.mutate(case = str_to_upper(col('name')))
    """

    string = _col_expr(string)
    return string.str.to_uppercase()

def str_to_lower(string : str):
    """
    Convert case of a string

    Parameters
    ----------
    string : str
        Convert case of this string

    Examples
    --------
    >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    >>> df.mutate(case = str_to_lower(col('name')))
    """

    string = _col_expr(string)
    return string.str.to_lowercase()


def str_replace_all(string : str, pattern : str, replacement : str):
    """
    Replace matched patterns in a string

    Parameters
    ----------
    string : str
        Input series to operate on
    pattern : str
        Pattern to look for

    Examples
    --------
    >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    >>> df.mutate(detect_single = str_detect('name', ['a']))
    >>> df.mutate(detect_multiple = str_detect('name', ['a', 'e']))
    """
    if isinstance(pattern, str):
        [pattern]
    
    string = _col_expr(string)

    exprs = (string.str.contains(p) for p in pattern)
    exprs = ft.reduce(lambda a, b : a & b, exprs)
   
    return exprs