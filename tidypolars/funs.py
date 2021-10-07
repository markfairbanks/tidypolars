import polars as pl
from polars import Expr

def _shift(expr, n, default):
    if default == None:
        return expr.shift(n)
    else:
        return expr.shift_and_fill(n, default)

def lag(expr, n: int = 1, default = None):
    return _shift(expr, n, default)

pl.Expr.lag = lag

def lead(expr, n: int = 1, default = None):
    return _shift(expr, -n, default)

pl.Expr.lead = lead