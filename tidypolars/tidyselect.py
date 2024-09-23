import polars as pl
import polars.selectors as cs

__all__ = ["contains", "ends_with", "everything", "starts_with", "where"]

def contains(match, ignore_case = True):
    """
    Contains a literal string

    Parameters
    ----------
    match : str
        String to match columns

    ignore_case : bool
        If TRUE, the default, ignores case when matching names.

    Examples
    --------
    >>> df = tp.tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
    >>> df.select(contains('c'))
    """
    if ignore_case == True:
        out = cs.matches(f"^*(?i){match}.*$")
    else:
        out = cs.contains(match)
    return out

def ends_with(match, ignore_case = True):
    """
    Ends with a suffix

    Parameters
    ----------
    match : str
        String to match columns

    ignore_case : bool
        If TRUE, the default, ignores case when matching names.

    Examples
    --------
    >>> df = tp.tibble({'a': range(3), 'b_code': range(3), 'c_code': ['a', 'a', 'b']})
    >>> df.select(ends_with('code'))
    """
    if ignore_case == True:
        out = cs.matches(f"^.*(?i){match}$")
    else:
        out = cs.ends_with(match)
    return out

def everything():
    """
    Selects all columns

    Examples
    --------
    >>> df = tp.tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
    >>> df.select(everything())
    """
    return cs.all()

def starts_with(match, ignore_case = True):
    """
    Starts with a prefix

    Parameters
    ----------
    match : str
        String to match columns
    ignore_case : bool
        If TRUE, the default, ignores case when matching names.

    Examples
    --------
    >>> df = tp.tibble({'a': range(3), 'add': range(3), 'sub': ['a', 'a', 'b']})
    >>> df.select(starts_with('a'))
    """
    if ignore_case == True:
        out = cs.matches(f"^(?i){match}.*$")
    else:
        out = cs.starts_with(match)
    return out

_col_types = {
    "date": cs.date(),
    "datetime": cs.datetime(),
    "float": cs.float(),
    "integer": cs.integer(),
    "numeric": cs.numeric(),
    "string": cs.string()
}

def where(col_type):
    """
    Select columns by type using a string

    Options:
        date, datetime, float, integer,
        numeric, string

    Examples
    --------
    >>> df.select(tp.where("integer"))
    """
    out = _col_types[col_type]
    return out