import polars as pl

__all__ = []

def _shift(expr, n, default):
    if default == None:
        return expr.shift(n)
    else:
        return expr.shift_and_fill(n, default)

def _lag(expr, n: int = 1, default = None):
    """
    Get lagging values

    Parameters
    ----------
    expr : Expr
        Column to operate on

    n : int
        Number of positions to lag by

    default : optional
        Value to fill in missing values

    Examples
    --------
    >>> df.mutate(lag_x = tp.lag(col('x')))
    >>> df.mutate(lag_x = col('x').lag())
    """
    return _shift(expr, n, default)

pl.Expr.lag = _lag

def _lead(expr, n: int = 1, default = None):
    """
    Get leading values

    Parameters
    ----------
    expr : Expr
        Column to operate on

    n : int
        Number of positions to lead by

    default : optional
        Value to fill in missing values

    Examples
    --------
    >>> df.mutate(lead_x = tp.lead(col('x')))
    >>> df.mutate(lead_x = col('x').lead())
    """
    return _shift(expr, -n, default)

pl.Expr.lead = _lead