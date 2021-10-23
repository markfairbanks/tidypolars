from tidypolars import col
import polars as pl
import functools as ft
from .utils import _col_expr
from .funs import is_not

__all__ = [
    "str_detect"
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
