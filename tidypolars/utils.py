import polars as pl
from operator import not_

__all__ = []

def _args_as_list(x):
    if len(x) == 0:
        return []
    elif isinstance(x[0], list):
        return x[0]
    elif isinstance(x[0], pl.Series):
        return x[0].to_list()
    else:
        return [*x]

# Convert kwargs to col() expressions with alias
def _kwargs_as_exprs(kwargs):
    return [expr.alias(key) for key, expr in kwargs.items()]

def _safe_len(x):
    if x == None:
        return 0
    else:
        return len(x)

def _uses_by(by):
    if isinstance(by, pl.Expr) | isinstance(by, str):
        return True
    elif isinstance(by, list):
        # Allow passing an empty list to `by`
        if _safe_len(by) == 0:
            return False
        else:
            return True
    else:
        return False

def _is_list_like(x):
    if isinstance(x, list) | isinstance(x, pl.Series):
        return True
    else:
        return False

#  Wrap all str inputs in col()  
def _col_exprs(x):
    if _is_list_like(x):
        return [_col_expr(val) for val in x]
    else:
        return [_col_expr(x)]

def _col_expr(x):
    if isinstance(x, pl.Expr) | isinstance(x, pl.Series):
        return x
    elif isinstance(x, str):
        return pl.col(x)
    else:
       raise ValueError("Invalid input for column selection") 

def _repeat(x, times):
    if not isinstance(x, list):
        x = [x]
    return x * times