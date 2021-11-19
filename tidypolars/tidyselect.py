import polars as pl

__all__ = ["contains", "ends_with", "everything", "starts_with"]

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
    >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
    >>> df.select(contains('c'))
    """
    if ignore_case == True:
        out = f"^*(?i){match}.*$"
    else:
        out = f"^*{match}.*$"
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
    >>> df = tp.Tibble({'a': range(3), 'b_code': range(3), 'c_code': ['a', 'a', 'b']})
    >>> df.select(ends_with('code'))
    """
    if ignore_case == True:
        out = f"^.*(?i){match}$"
    else:
        out = f"^.*{match}$"
    return out

def everything():
    """
    Selects all columns

    Examples
    --------
    >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
    >>> df.select(everything())
    """
    return "*"

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
    >>> df = tp.Tibble({'a': range(3), 'add': range(3), 'sub': ['a', 'a', 'b']})
    >>> df.select(starts_with('a'))
    """
    if ignore_case == True:
        out = f"^(?i){match}.*$"
    else:
        out = f"^{match}.*$"
    return out