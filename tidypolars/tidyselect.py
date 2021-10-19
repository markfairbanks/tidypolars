import tidypolars as tp
from tidypolars import col
import polars as pl

__all__ = ["contains", "ends_with", "everything", "starts_with" ]

def contains(match: str, ignorecase = True):
    """
    Contains a literal string.

    Parameters
    ----------
    match : str
        String to match columns

    Examples
    --------
    >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
    >>> df.select(contains('c'))
    """
    if ignorecase == True:
        out = col(f"^*(?i){match}.*$")
    else:
        out = col(f"^*{match}.*$")
    return out

def ends_with(match: str, ignorecase = True):
    """
    Ends with a suffix.

    Parameters
    ----------
    match : str
        String to match columns

    Examples
    --------
    >>> df = tp.Tibble({'a': range(3), 'b_code': range(3), 'c_code': ['a', 'a', 'b']})
    >>> df.select(ends_with('code'))
    """
    if ignorecase == True:
        out = col(f"^*(?i){match}$")
    else:
        out = col(f"^*{match}$")
    return out

def everything():
    """
    Selects all columns.

    Examples
    --------
    >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
    >>> df.select(everything())
    """
    return pl.all()

def starts_with(match: str, ignorecase = True):
    """
    Starts with a prefix.

    Parameters
    ----------
    match : str
        String to match columns

    Examples
    --------
    >>> df = tp.Tibble({'a': range(3), 'add': range(3), 'sub': ['a', 'a', 'b']})
    >>> df.select(starts_with('a'))
    """
    if ignorecase == True:
        out = col(f"^(?i){match}.*$")
    else:
        out = col(f"^{match}.*$")

    return out