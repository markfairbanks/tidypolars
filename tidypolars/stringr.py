from tidypolars import col
import polars as pl
import functools as ft
from .utils import _col_expr
from .funs import is_not

__all__ = [
    "str_detect"
    ]


def str_detect(string : str, pattern : str, negate: bool = False):
    if isinstance(pattern, str):
        [pattern]
    
    string = _col_expr(string)

    exprs = (string.str.contains(p) for p in pattern)
    exprs = ft.reduce(lambda a, b : a & b, exprs)
    if negate:
        exprs = exprs.is_not()
    
    return exprs
