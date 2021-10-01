import polars as pl
import numpy as np
import functools as ft

import typing as tp
from typing import Union

col = pl.col

def as_tidyframe(df):
    df.__class__ = tidyframe
    return df

def col_expr(x):
    if isinstance(x, pl.Expr):
        return x
    elif isinstance(x, str):
        return col(x)
    else:
       raise ValueError("Invalid input for column selection") 
    
def col_exprs(x):
    if (is_list_like(x)):
        return [col_expr(val) for val in x]
    else:
        return [col_expr(x)]
    
def is_list_like(x):
    if (isinstance(x, list)) | (isinstance(x, np.ndarray)):
        return True
    else:
        return False
    
# Helpful for pivot_longer/_wider
def arg_as_list(x: Union[str, list]) -> list:
    if not is_list_like(x):
        x = [x]
    else:
        x = x.copy()

    return x

class tidyframe(pl.DataFrame):
    def arrange(self, *args, desc: Union[bool, tp.List[bool]] = False) -> "tf.tidyframe":
        """
        Arrange/sort rows

        Parameters
        ----------
        *args : Union[str, Expr]
            Columns to sort by

        desc : Union[bool, List[bool]] = False
            Should columns be ordered in descending order

        Returns
        -------
            tf.tidyframe

        Examples
        --------
        df = pl.DataFrame({'x': ['a', 'a', 'b'], 'y': range(3)})
        
        # Arrange in ascending order
        df.arrange('x', 'y')
        
        # Arrange some columns descending
        df.arrange('x', 'y', desc = [True, False])
        """
        exprs = list(args)
        return self.sort(exprs, reverse = desc).pipe(as_tidyframe)
    
    def filter(self, *args) -> "tf.tidyframe":
        """
        Filter rows on one or more conditions

        Parameters
        ----------
        *args : Expr
            Conditions to filter by

        Returns
        -------
            tf.tidyframe

        Examples
        --------
        df = tf.tidyframe(
            {'a': range(3),
             'b': range(3),
             'c': ['a', 'a', 'b']}
        )
        
        df.filter(col('a') < 2, col('c') == 'a')
        """
        args = list(args)
        exprs = ft.reduce(lambda a, b: a & b, args)
        return super().filter(exprs).pipe(as_tidyframe)
    
    def mutate(self, **kwargs) -> "tf.tidyframe":
        """
        Add or modify columns

        Parameters
        ----------
        **kwargs : Expr
            Column expressions to add or modify

        Returns
        -------
            tf.tidyframe

        Examples
        --------
        df = tf.tidyframe(
            {'a': range(3),
             'b': range(3),
             'c': ['a', 'a', 'b']}
        )
        
        (
            df
            .mutate(double_a = col('a') * 2,
                    a_plus_b = col('a') + col('b'))
        )
        """
        exprs = [expr.alias(key) for key, expr in kwargs.items()]
        return self.with_columns(exprs).pipe(as_tidyframe)
    
    def pipe(self, fn, *args, **kwargs):
        return fn(self, *args, **kwargs)
    
    def relocate(self, *args, before: str = None, after: str = None) -> "tf.tidyframe":
        """
        Move a column or columns to a new position

        Parameters
        ----------
        **args : str
            Columns to move

        Returns
        -------
            tf.tidyframe

        Examples
        --------
        df = tf.tidyframe(
            {'a': range(3),
             'b': range(3),
             'c': ['a', 'a', 'b']}
        )
        
        df.relocate('a', before = 'c')

        df.relocate('b', after = 'c')
        """
        move_cols = np.array(list(args))

        if len(move_cols) == 0:
            return self
        else:
            if (before != None) & (after != None):
                raise ValueError("Cannot provide both before and after")

            all_cols = np.array(self.columns)
            all_locs = np.arange(0, len(all_cols))
            
            move_cols = col_exprs(move_cols)
            move_cols = self.select(move_cols).columns
            move_locs = all_locs[np.isin(all_cols, move_cols)]

            if (before == None) & (after == None):
                before_loc = 0
            elif before != None:
                before = col_exprs(before)
                before = self.select(before).columns[0]
                before_loc = all_locs[all_cols == before]
            else:
                after = col_exprs(after)
                after = self.select(after).columns[0]
                before_loc = all_locs[all_cols == after] + 1

            before_locs = np.arange(0, before_loc)
            after_locs = np.arange(before_loc, len(all_cols))

            before_locs = np.setdiff1d(before_locs, move_locs)
            after_locs = np.setdiff1d(after_locs, move_locs)

            final_order = np.concatenate((before_locs, move_locs, after_locs))

            ordered_cols = all_cols[final_order]

            return self.select(ordered_cols)
    
    def select(self, *args) -> "tf.tidyframe":
        """
        Select or drop columns

        Parameters
        ----------
        **args : str
            Columns to select

        Returns
        -------
            tf.tidyframe

        Examples
        --------
        df = tf.tidyframe(
            {'a': range(3),
             'b': range(3),
             'c': ['a', 'a', 'b']}
        )
        
        df.relocate('a', before = 'c')

        df.relocate('b', after = 'c')
        """
        arg = list(args)
        args = [[arg] if not is_list_like(arg) else arg for arg in args]
        args = np.concatenate(args)
        return super().select(args).pipe(as_tidyframe)