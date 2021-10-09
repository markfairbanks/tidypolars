import polars as pl
from polars import Expr, when

def _shift(expr, n, default):
    if default == None:
        return expr.shift(n)
    else:
        return expr.shift_and_fill(n, default)

def _args_as_list(x):
    if len(x) == 0:
        return []
    elif isinstance(x[0], list):
        return x[0]
    elif isinstance(x[0], pl.Series):
        return list(x[0])
    else:
        return [*x]

def _case(*args, default=None):
    args = _args_as_list(args)
    for logic, answer in args:
        out = when(logic).then(answer).otherwise(default)
        return out

def case_when(*args, default = None):
    """
    Use multiple if/else statements in one call

    Parameters
    ----------
    *args : Expr
        Column expressions and logic to apply

    default : optional
        Value to fill in missing values

    Examples
    --------
    >>> df = tp.Tibble({'x' : ['a', 'b', 'c'], 'y' : range(3)})
    >>> df.mutate(
    >>>     single_case =  tp.case_when((col('y') > 1, "greater than one"), default = "less than one"), 
    >>>     multi_case = tp.case_when((col('y') == 1, "one"), (col('y') == 2, "two"), default="zero"),
    >>>     complex_case = tp.case_when(
    >>>         (col('x').lag() == 'b', "previous is b"), 
    >>>         (col('x').lead() == 'b', "next is b"), 
    >>>         default = "others"))
    """
    # TODO: Create for series
    if len(args) == 0:
        raise ValueError("case_when must have at least one argument. See examples in documentation.")
    for index, obj in enumerate(args):
        if index == 0:
            chained_case = _case(obj, default = default)
        else:
            chained_case = _case(obj, default = chained_case)
    return chained_case

def lag(expr, n: int = 1, default = None):
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

pl.Expr.lag = lag

def lead(expr, n: int = 1, default = None):
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

pl.Expr.lead = lead