import polars as pl

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

def _no_by(gb):
    if isinstance(gb, pl.Expr) | isinstance(gb, str) | isinstance(gb, list):
        return False
    else:
        return True

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