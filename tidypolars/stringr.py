import polars as pl
import functools as ft
from .utils import _args_as_list, _col_expr

__all__ = [
    "paste",
    "paste0",
    "str_detect", 
    "str_extract",
    "str_length",
    "str_remove_all",
    "str_remove", 
    "str_replace_all", 
    "str_replace", 
    "str_sub",
    "str_to_lower", 
    "str_to_upper",
    "str_trim"
]

def paste(*args, sep = ' '):
    """
    Concatenate strings together

    Parameters
    ----------
    args : Expr, str
        Columns and or strings to concatenate

    Examples
    --------
    >>> df = tp.Tibble(x = ['a', 'b', 'c'])
    >>> df.mutate(x_end = tp.paste(col('x'), 'end', sep = '_'))
    """
    args = _args_as_list(args)
    args = [pl.lit(arg) if not isinstance(arg, pl.Expr) else arg for arg in args]
    curlies = ['{}'] * len(args)
    string_format = sep.join(curlies)
    return pl.format(string_format, *args)

def paste0(*args):
    """
    Concatenate strings together with no separator

    Parameters
    ----------
    args : Expr, str
        Columns and or strings to concatenate

    Examples
    --------
    >>> df = tp.Tibble(x = ['a', 'b', 'c'])
    >>> df.mutate(xend = tp.paste0(col('x'), 'end'))
    """
    return paste(*args, sep = '')

def str_detect(string, pattern, negate = False):
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
    >>> df.mutate(x = str_detect('name', 'a'))
    >>> df.mutate(x = str_detect('name', ['a', 'e']))
    """
    if isinstance(pattern, str):
        pattern = [pattern]
    
    string = _col_expr(string)

    exprs = (string.str.contains(p) for p in pattern)
    exprs = ft.reduce(lambda a, b : a & b, exprs)
    if negate:
        exprs = exprs.is_not()
    
    return exprs

def str_extract(string, pattern):
    """
    Extract the target capture group from provided patterns

    Parameters
    ----------
    string : str
        Input series to operate on
    pattern : str
        Pattern to look for

    Examples
    --------
    >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    >>> df.mutate(x = str_extract(col('name'), 'e'))
    """
    string = _col_expr(string)
    return string.str.extract(pattern, 0)

def str_length(string):
    """
    Length of a string

    Parameters
    ----------
    string : str
        Input series to operate on

    Examples
    --------
    >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    >>> df.mutate(x = str_length(col('name')))
    """
    string = _col_expr(string)
    return string.str.lengths()

def str_sub(string, start = 0, end = None):
    """
    Extract portion of string based on start and end inputs

    Parameters
    ----------
    string : str
        Input series to operate on
    start : int
        First position of the character to return
    end : int
        Last position of the character to return

    Examples
    --------
    >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    >>> df.mutate(x = str_sub(col('name'), 0, 3))
    """
    string = _col_expr(string) 
    return string.str.slice(start, end)

def str_remove_all(string, pattern):
    """
    Removes all matched patterns in a string

    Parameters
    ----------
    string : str
        Input series to operate on
    pattern : str
        Pattern to look for

    Examples
    --------
    >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    >>> df.mutate(x = str_remove_all(col('name'), 'a'))
    """
    return str_replace_all(string, pattern, "")

def str_remove(string, pattern):
    """
    Removes the first matched patterns in a string

    Parameters
    ----------
    string : str
        Input series to operate on
    pattern : str
        Pattern to look for

    Examples
    --------
    >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    >>> df.mutate(x = str_remove(col('name'), 'a'))
    """
    return str_replace(string, pattern, "")

def str_replace_all(string, pattern, replacement):
    """
    Replaces all matched patterns in a string

    Parameters
    ----------
    string : str
        Input series to operate on
    pattern : str
        Pattern to look for
    replacement : str
        String that replaces anything that matches the pattern

    Examples
    --------
    >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    >>> df.mutate(x = str_replace_all(col('name'), 'a', 'A'))
    """
    string = _col_expr(string)
    return string.str.replace_all(pattern, replacement)

def str_replace(string, pattern, replacement):
    """
    Replaces the first matched patterns in a string

    Parameters
    ----------
    string : str
        Input series to operate on
    pattern : str
        Pattern to look for
    replacement : str
        String that replaces anything that matches the pattern

    Examples
    --------
    >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    >>> df.mutate(x = str_replace(col('name'), 'a', 'A'))
    """
    string = _col_expr(string)
    return string.str.replace(pattern, replacement)

def str_to_lower(string):
    """
    Convert case of a string

    Parameters
    ----------
    string : str
        Convert case of this string

    Examples
    --------
    >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    >>> df.mutate(x = str_to_lower(col('name')))
    """
    string = _col_expr(string)
    return string.str.to_lowercase()

def str_to_upper(string):
    """
    Convert case of a string

    Parameters
    ----------
    string : str
        Convert case of this string

    Examples
    --------
    >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
    >>> df.mutate(x = str_to_upper(col('name')))
    """
    string = _col_expr(string)
    return string.str.to_uppercase()

def str_trim(string, side = "both"):
    """
    Trim whitespace

    Parameters
    ----------
    string : Expr, Series
        Column or series to operate on
    side : str
        One of:
            * "both"
            * "left"
            * "right"

    Examples
    --------
    >>> df = tp.Tibble(x = [' a ', ' b ', ' c '])
    >>> df.mutate(x = tp.str_trim(col('x')))
    """
    string = _col_expr(string)
    if side == "both":
        out = _str_trim_right(_str_trim_left(string))
    elif side == "left":
        out = _str_trim_left(string)
    elif side == "right":
        out = _str_trim_right(string)
    else:
        raise ValueError("side must be one of 'both', 'left', or 'right'")
    return out

def _str_trim_left(x):
    """
    Remove leading whitespace.
    """
    return x.str.replace(r"^\s*", "")

def _str_trim_right(x):
    """
    Remove trailing whitespace.
    """
    return x.str.replace(r"[ \t]+$", "")
