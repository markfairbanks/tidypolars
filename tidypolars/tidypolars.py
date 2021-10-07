import polars as pl
from polars import col, Expr, Series
import functools as ft
from typing import Dict, List, Union

from .funs import *

def _as_Tibble(df):
    df.__class__ = Tibble
    return df

def _as_DataFrame(df):
    df.__class__ = pl.DataFrame
    return df
  
def _is_list_like(x):
    if isinstance(x, list) | isinstance(x, pl.Series):
        return True
    else:
        return False

def _as_list(x):
    if isinstance(x, list):
        return x.copy()
    elif isinstance(x, str):
        return [x]
    else:
        return list(x)

def _args_as_list(x):
    if len(x) == 0:
        return []
    elif isinstance(x[0], list):
        return x[0]
    elif isinstance(x[0], pl.Series):
        return list(x[0])
    else:
        return [*x]

# Convert kwargs to col() expressions with alias
def _kwargs_as_exprs(kwargs):
    return [expr.alias(key) for key, expr in kwargs.items()]

def _no_groupby(gb):
    if isinstance(gb, Expr) | isinstance(gb, str) | isinstance(gb, list):
        return False
    else:
        return True

class Tibble(pl.DataFrame):
    def __repr__(self) -> str:
        df = _as_DataFrame(self)
        return df.__str__()

    def arrange(self, *args, desc: bool = False):
        exprs = _args_as_list(args)
        return self.sort(exprs, reverse = desc).pipe(_as_Tibble)

    def bind_cols(self, df: "tp.Tibble"):
        return self.hstack(df).pipe(_as_Tibble)
    
    def bind_rows(self, df: "tp.Tibble"):
        return self.vstack(df).pipe(_as_Tibble)

    def distinct(self, *args):
        # TODO: Create for series
        args = _args_as_list(args)

        if len(args) == 0:
            df = self.drop_duplicates()
        else:
            df = self.select(args).drop_duplicates()
        
        return df.pipe(_as_Tibble)
    
    def head(self, n = 5, *args, groupby = None):
        return self.slice_tail(n, groupby = groupby)

    def filter(
        self, *args,
        groupby: Union[str, Expr, List[str], List[Expr]] = None
    ):
        df = _as_DataFrame(self)
        args = _args_as_list(args)
        exprs = ft.reduce(lambda a, b: a & b, args)

        if _no_groupby(groupby):
            df = df.filter(exprs)
        else:
            df = df.groupby(groupby).apply(lambda x: x.filter(exprs))
        
        return df.pipe(_as_Tibble)

    def mutate(
        self,
        *args,
        groupby: Union[str, Expr, List[str], List[Expr]] = None,
        **kwargs
    ):
        exprs = _args_as_list(args) + _kwargs_as_exprs(kwargs)
        if _no_groupby(groupby):
            out = self.with_columns(exprs)
        else:
            out = self.groupby(groupby).apply(lambda x: x.with_columns(exprs))
        
        return out.pipe(_as_Tibble)

    def pull(self, var: str = None):
        if var == None:
            var = self.columns[-1]
        
        return self.get_column(var)
    
    def relocate(self, *args, before: str = None, after: str = None):
        move_cols = pl.Series(list(args))

        if len(move_cols) == 0:
            return self
        else:
            if (before != None) & (after != None):
                raise ValueError("Cannot provide both before and after")

            all_cols = pl.Series(self.columns)
            all_locs = pl.Series(range(len(all_cols)))
            
            move_cols = pl.Series(self.select(move_cols).columns)
            move_locs = all_locs[all_cols.is_in(move_cols)]

            if (before == None) & (after == None):
                before_loc = 0
            elif before != None:
                before = self.select(before).columns[0]
                before_loc = all_locs[all_cols == before][0]
            else:
                after = self.select(after).columns[0]
                before_loc = all_locs[all_cols == after][0] + 1

            before_locs = pl.Series(range(before_loc))
            after_locs = pl.Series(range(before_loc, len(all_cols)))

            before_locs = before_locs[~before_locs.is_in(move_locs)]
            after_locs = after_locs[~after_locs.is_in(move_locs)]

            final_order = before_locs.cast(int)
            final_order.append(move_locs.cast(int))
            final_order.append(after_locs.cast(int))

            ordered_cols = all_cols.take(final_order)

            return self.select(ordered_cols)
    
    def rename(self, mapping: Dict[str, str]):
        df = _as_DataFrame(self)
        return df.rename(mapping).pipe(_as_Tibble)
    
    def select(self, *args):
        args = _args_as_list(args)
        return super().select(args).pipe(_as_Tibble)

    def slice(self, *args, groupby = None):
        rows = _args_as_list(args)
        if _no_groupby(groupby):
            df = self[rows]
        else:
            df = self.groupby(groupby).apply(lambda x: x[rows])
        return df.pipe(_as_Tibble)

    def slice_head(self, n: int = 5, *args, groupby = None):
        df = _as_DataFrame(self)
        args = _args_as_list(args)
        col_order = df.columns
        if _no_groupby(groupby):
            df = df.head(n)
        else:
            df = df.groupby(groupby).head(n)
        return df.pipe(_as_Tibble).select(col_order)

    def slice_tail(self, n: int = 5, *args, groupby = None):
        df = _as_DataFrame(self)
        args = _args_as_list(args)
        col_order = df.columns
        if _no_groupby(groupby):
            df = df.tail(n)
        else:
            df = df.groupby(groupby).tail(n)
        return df.pipe(_as_Tibble).select(col_order)
    
    def summarize(
        self, *args,
        groupby: Union[str, Expr, List[str], List[Expr]] = None,
        **kwargs
    ):
        exprs = _args_as_list(args) + _kwargs_as_exprs(kwargs)
        df = _as_DataFrame(self)

        if _no_groupby(groupby):
            out = df.select(exprs)
        else:
            out = df.groupby(groupby).agg(exprs)
        
        return out.pipe(_as_Tibble)

    def tail(self, n = 5, *args, groupby = None):
        return self.slice_tail(n, groupby = groupby)