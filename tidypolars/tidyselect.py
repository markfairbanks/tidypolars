import polars as pl

__all__ = ["col_contains", "col_ends_with", "col_everything", "col_starts_with" ]

def col_contains(match: str, ignore_case = True):
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
    >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
    >>> df.select(col_contains('c'))
    """
    if ignore_case == True:
        out = pl.col(f"^*(?i){match}.*$")
    else:
        out = pl.col(f"^*{match}.*$")
    return out

def col_ends_with(match: str, ignore_case = True):
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
    >>> df = tp.Tibble({'a': range(3), 'b_code': range(3), 'c_code': ['a', 'a', 'b']})
    >>> df.select(col_ends_with('code'))
    """
    if ignore_case == True:
        out = pl.col(f"^*(?i){match}$")
    else:
        out = pl.col(f"^*{match}$")
    return out

def col_everything():
    """
    Selects all columns

    Examples
    --------
    >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
    >>> df.select(col_everything())
    """
    return pl.all()

def col_starts_with(match: str, ignore_case = True):
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
    >>> df = tp.Tibble({'a': range(3), 'add': range(3), 'sub': ['a', 'a', 'b']})
    >>> df.select(col_starts_with('a'))
    """
    if ignore_case == True:
        out = pl.col(f"^(?i){match}.*$")
    else:
        out = pl.col(f"^{match}.*$")

    return out