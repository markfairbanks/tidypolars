import polars as pl
from .tibble_df import from_polars, tibble
from .utils import (
    _as_list,
    _col_expr,
    _col_exprs,
    _is_constant,
    _is_list,
    _is_iterable,
    _is_series,
    _is_string,
    _str_to_lit
)

__all__ = [
    # General functions
    "abs",
    "across",
    "case_when",
    "coalesce",
    "floor",
    "if_else",
    "lag", "lead",
    "log", "log10",
    "read_csv", "read_parquet",
    "rep",
    "replace_null",
    "round",
    "row_number",
    "sqrt",

    # Agg stats
    "cor", "cov", "count", "first", "last", "length",
    "max", "mean", "median", "min", "n",
    "n_distinct", "quantile", "sd", "sum", "var",

    # Predicates
    "between", "is_finite", "is_in", "is_infinite",
    "is_nan", "is_not", "is_not_in", "is_not_null", "is_null",

    # Type conversion
    "as_boolean", "as_float", "as_integer", "as_string",
    "cast"
]

def across(cols, fn = lambda x: x, names_prefix = None):
    """
    Apply a function across a selection of columns

    Parameters
    ----------
    cols : list
        Columns to operate on
    fn : lambda
        A function or lambda to apply to each column
    names_prefix : Optional - str
        Prefix to append to changed columns

    Examples
    --------
    >>> df = tp.tibble(x = ['a', 'a', 'b'], y = range(3), z = range(3))
    >>> df.mutate(across(['y', 'z'], lambda x: x * 2))
    >>> df.mutate(across(tp.Int64, lambda x: x * 2, names_prefix = "double_"))
    >>> df.summarize(across(['y', 'z'], tp.mean), by = 'x')
    """
    _cols = _col_exprs(_as_list(cols))
    exprs = [fn(_col) for _col in _cols]
    if names_prefix != None:
        exprs = [expr.name.prefix(names_prefix) for expr in exprs]
    return exprs

def as_boolean(x):
    """
    Convert to a boolean

    Parameters
    ----------
    x : Expr
        Column to operate on

    Examples
    --------
    >>> df.mutate(bool_x = tp.as_boolean(col('x')))
    """
    x = _col_expr(x)
    return x.cast(pl.Boolean)

def as_float(x):
    """
    Convert to float. Defaults to Float64.

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(float_x = tp.as_float(col('x')))
    """
    x = _col_expr(x)
    return x.cast(pl.Float64)

def as_integer(x):
    """
    Convert to integer. Defaults to Int64.

    Parameters
    ----------
    x : Expr
        Column to operate on

    Examples
    --------
    >>> df.mutate(int_x = tp.as_integer(col('x')))
    """
    x = _col_expr(x)
    return x.cast(pl.Int64)

def as_string(x):
    """
    Convert to string. Defaults to Utf8.

    Parameters
    ----------
    x : Expr
        Column to operate on

    Examples
    --------
    >>> df.mutate(string_x = tp.as_string(col('x')))
    """
    x = _col_expr(x)
    return x.cast(pl.Utf8)

def abs(x):
    """
    Absolute value

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(abs_x = tp.abs('x'))
    >>> df.mutate(abs_x = tp.abs(col('x')))
    """
    x = _col_expr(x)
    return x.abs()

def between(x, left, right):
    """
    Test if values of a column are between two values

    Parameters
    ----------
    x : Expr, Series
        Column to operate on
    left : int
        Value to test if column is greater than or equal to
    right : int
        Value to test if column is less than or equal to

    Examples
    --------
    >>> df = tp.tibble(x = range(4))
    >>> df.filter(tp.between(col('x'), 1, 3))
    """
    x = _col_expr(x)
    return x.is_between(left, right)

def case_when(*args, _default = pl.Null):
    """
    Case when

    Parameters
    ----------
    expr : Expr
        A logical expression

    Examples
    --------
    >>> df = tp.tibble(x = range(1, 4))
    >>> df.mutate(
    >>>    case_x = tp.case_when(col('x') < 2, 1,
    >>>                          col('x') < 3, 2,
    >>>                          _default = 0)
    >>> )
    """
    conditions = [args[i] for i in range(0, len(args), 2)]
    values = [args[i] for i in range(1, len(args), 2)]
    values = [_str_to_lit(value) for value in values]
    for i in range(len(conditions)):
        if i == 0:
            expr = pl.when(conditions[i]).then(values[i])
        else:
            expr = expr.when(conditions[i]).then(values[i])
    _default = _str_to_lit(_default)
    expr = expr.otherwise(_default)
    return expr

def cast(x, dtype):
    """
    General type conversion.

    Parameters
    ----------
    x : Expr, Series
        Column to operate on
    dtype : DataType
        Type to convert to

    Examples
    --------
    >>> df.mutate(float_x = tp.cast(col('x'), tp.Float64))
    """
    x = _col_expr(x)
    return x.cast(dtype)

def coalesce(*args):
    """
    Coalesce missing values

    Parameters
    ----------
    args : Expr
        Columns to coalesce

    Examples
    --------
    >>> df.mutate(coalesce_xy = tp.coalesce(col('x'), col('y')))
    """
    args = _as_list(args)
    expr = if_else(args[0].is_null(), args[1], args[0])
    if len(args) > 2:
        locs = range(2, len(args))
        for i in locs:
            expr = if_else(expr.is_null(), args[i], expr)
    return expr

def cor(x, y, method = 'pearson'):
    """
    Find the correlation of two columns

    Parameters
    ----------
    x : Expr
        A column
    y : Expr
        A column
    method : str
        Type of correlation to find. Either 'pearson' or 'spearman'.

    Examples
    --------
    >>> df.summarize(cor = tp.cor(col('x'), col('y')))
    """
    if pl.Series([method]).is_in(['pearson', 'spearman']).not_().item():
        ValueError("`method` must be either 'pearson' or 'spearman'")
    return pl.corr(x, y, method = method)

def cov(x, y):
    """
    Find the covariance of two columns

    Parameters
    ----------
    x : Expr
        A column
    y : Expr
        A column

    Examples
    --------
    >>> df.summarize(cov = tp.cov(col('x'), col('y')))
    """
    return pl.cov(x, y)

def count(x):
    """
    Number of observations in each group

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.summarize(count = tp.count(col('x')))
    """
    x = _col_expr(x)
    return x.count()

def first(x):
    """
    Get first value

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.summarize(first_x = tp.first('x'))
    >>> df.summarize(first_x = tp.first(col('x')))
    """
    x = _col_expr(x)
    return x.first()

def floor(x):
    """
    Round numbers down to the lower integer

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(floor_x = tp.floor(col('x')))
    """
    x = _col_expr(x)
    return x.floor()

def if_else(condition, true, false):
    """
    If Else

    Parameters
    ----------
    condition : Expr
        A logical expression
    true :
        Value if the condition is true
    false :
        Value if the condition is false

    Examples
    --------
    >>> df = tp.tibble(x = range(1, 4))
    >>> df.mutate(if_x = tp.if_else(col('x') < 2, 1, 2))
    """
    return case_when(condition, true, _default = false)

def is_finite(x):
    """
    Test if values of a column are finite

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df = tp.tibble(x = [1.0, float('inf')])
    >>> df.filter(tp.is_finite(col('x')))
    """
    x = _col_expr(x)
    return x.is_finite()

def is_in(x, y):
    """
    Test if values of a column are in a list of values

    Parameters
    ----------
    x : Expr, Series
        Column to operate on
    y : list
        List to test against

    Examples
    --------
    >>> df = tp.tibble(x = range(3))
    >>> df.filter(tp.is_in(col('x'), [1, 2]))
    """
    x = _col_expr(x)
    return x.is_in(y)

def is_infinite(x):
    """
    Test if values of a column are infinite

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df = tp.tibble(x = [1.0, float('inf')])
    >>> df.filter(tp.is_infinite(col('x')))
    """
    x = _col_expr(x)
    return x.is_infinite()

def is_not(x):
    """
    Flip values of a boolean series

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df = tp.tibble(x = range(3))
    >>> df.filter(tp.is_not(col('x') < 2))
    """
    x = _col_expr(x)
    return x.not_()

def is_nan(x):
    """
    Test if values of a column are nan

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df = tp.tibble(x = range(3))
    >>> df.filter(tp.is_nan(col('x')))
    """
    x = _col_expr(x)
    return x.is_nan()

def is_not_in(x, y):
    """
    Test if values of a column are not in a list of values

    Parameters
    ----------
    x : Expr, Series
        Column to operate on
    y : list
        List to test against

    Examples
    --------
    >>> df = tp.tibble(x = range(3))
    >>> df.filter(tp.is_not_in(col('x'), [1, 2]))
    """
    x = _col_expr(x)
    return x.is_in(y).not_()

def is_not_null(x):
    """
    Test if values of a column are not null

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df = tp.tibble(x = range(3))
    >>> df.filter(tp.is_not_null(col('x'), [1, 2]))
    """
    x = _col_expr(x)
    return x.is_null().not_()

def is_null(x):
    """
    Test if values of a column are null

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df = tp.tibble(x = range(3))
    >>> df.filter(tp.is_null(col('x')))
    """
    x = _col_expr(x)
    return x.is_null()

def lag(x, n: int = 1, default = None):
    """
    Get lagging values

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    n : int
        Number of positions to lag by

    default : optional
        Value to fill in missing values

    Examples
    --------
    >>> df.mutate(lag_x = tp.lag(col('x')))
    >>> df.mutate(lag_x = tp.lag('x'))
    """
    x = _col_expr(x)
    return x.shift(n, fill_value = default)

def last(x):
    """
    Get last value

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.summarize(last_x = tp.last('x'))
    >>> df.summarize(last_x = tp.last(col('x')))
    """
    x = _col_expr(x)
    return x.last()

def lead(x, n: int = 1, default = None):
    """
    Get leading values

    Parameters
    ----------
    x : Expr, Series
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
    x = _col_expr(x)
    return x.shift(-n, fill_value = default)

def length(x):
    """
    Number of observations in each group

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.summarize(length = tp.length(col('x')))
    """
    x = _col_expr(x)
    return x.count()

def log(x):
    """
    Compute the natural logarithm of a column

    Parameters
    ----------
    x : Expr
        Column to operate on

    Examples
    --------
    >>> df.mutate(log = tp.log('x'))
    """
    x = _col_expr(x)
    return x.log()

def log10(x):
    """
    Compute the base 10 logarithm of a column

    Parameters
    ----------
    x : Expr
        Column to operate on

    Examples
    --------
    >>> df.mutate(log = tp.log10('x'))
    """
    x = _col_expr(x)
    return x.log10()

def max(x):
    """
    Get column max

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.summarize(max_x = tp.max('x'))
    >>> df.summarize(max_x = tp.max(col('x')))
    """
    x = _col_expr(x)
    return x.max()

def mean(x):
    """
    Get column mean

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.summarize(mean_x = tp.mean('x'))
    >>> df.summarize(mean_x = tp.mean(col('x')))
    """
    x = _col_expr(x)
    return x.mean()

def median(x):
    """
    Get column median

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.summarize(median_x = tp.median('x'))
    >>> df.summarize(median_x = tp.median(col('x')))
    """
    x = _col_expr(x)
    return x.median()

def min(x):
    """
    Get column minimum

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.summarize(min_x = tp.min('x'))
    >>> df.summarize(min_x = tp.min(col('x')))
    """
    x = _col_expr(x)
    return x.min()

def n():
    """
    Number of observations in each group

    Examples
    --------
    >>> df.summarize(count = tp.n())
    """
    return pl.len()

def n_distinct(x):
    """
    Get number of distinct values in a column

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.summarize(min_x = tp.n_distinct('x'))
    >>> df.summarize(min_x = tp.n_distinct(col('x')))
    """
    x = _col_expr(x)
    return x.n_unique()

def quantile(x, quantile = .5):
    """
    Get number of distinct values in a column

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    quantile : float
        Quantile to return

    Examples
    --------
    >>> df.summarize(quantile_x = tp.quantile('x', .25))
    """
    x = _col_expr(x)
    return x.quantile(quantile)

def read_csv(file: str,
             *args,
             **kwargs):
    """Simple wrapper around polars.read_csv"""
    return pl.read_csv(file, *args, **kwargs).pipe(from_polars)

def read_parquet(source: str,
                 *args,
                 **kwargs):
    """Simple wrapper around polars.read_parquet"""
    return pl.read_parquet(source, *args, **kwargs).pipe(from_polars)

def rep(x, times = 1):
    """
    Replicate the values in x

    Parameters
    ----------
    x : const, Series
        Value or Series to repeat
    times : int
        Number of times to repeat

    Examples
    --------
    >>> tp.rep(1, 3)
    >>> tp.rep(pl.Series(range(3)), 3)
    """
    if _is_constant(x):
        out = [x]
    elif _is_series(x):
        out = x.to_list()
    elif _is_list(x):
        out = x
    elif isinstance(x, tibble):
        out = pl.concat([x for i in range(times)]).pipe(from_polars)
    elif _is_iterable(x):
        out = list(x)
    else:
        ValueError("Incompatible type")
    if _is_list(out):
        out = pl.Series(out * times)
    return out

def replace_null(x, replace = None):
    """
    Replace null values

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df = tp.tibble(x = [0, None], y = [None, None])
    >>> df.mutate(x = tp.replace_null(col('x'), 1))
    """
    if replace == None: return x
    return x.fill_null(replace)

def round(x, decimals = 0):
    """
    Get column standard deviation

    Parameters
    ----------
    x : Expr, Series
        Column to operate on
    decimals : int
        Decimals to round to

    Examples
    --------
    >>> df.mutate(x = tp.round(col('x')))
    """
    x = _col_expr(x)
    return x.round(decimals)

def row_number():
    """
    Return row number

    Examples
    --------
    >>> df.mutate(row_num = tp.row_number())
    """
    return pl.int_range(0, pl.len()) + 1

def sd(x):
    """
    Get column standard deviation

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.summarize(sd_x = tp.sd('x'))
    >>> df.summarize(sd_x = tp.sd(col('x')))
    """
    x = _col_expr(x)
    return x.std()

def sqrt(x):
    """
    Get column square root

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.mutate(sqrt_x = tp.sqrt('x'))
    """
    x = _col_expr(x)
    return x.sqrt()

def sum(x):
    """
    Get column sum

    Parameters
    ----------
    x : Expr, Series
        Column to operate on

    Examples
    --------
    >>> df.summarize(sum_x = tp.sum('x'))
    >>> df.summarize(sum_x = tp.sum(col('x')))
    """
    x = _col_expr(x)
    return x.sum()

def var(x):
    """
    Get column variance

    Parameters
    ----------
    x : Expr
        Column to operate on

    Examples
    --------
    >>> df.summarize(sum_x = tp.var('x'))
    >>> df.summarize(sum_x = tp.var(col('x')))
    """
    x = _col_expr(x)
    return x.var()
