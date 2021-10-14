import polars as pl
import functools as ft
from typing import Dict, Union
import typing as typ
from .utils import (
    _args_as_list,
    _kwargs_as_exprs,
    _no_groupby,
    _col_exprs
)
from .reexports import *

__all__ = [
    "Tibble",
    "from_pandas", "from_polars"
]

def from_polars(df):
    """
    Convert from polars DataFrame to Tibble

    Parameters
    ----------
    df : DataFrame
        pl.DataFrame to convert to a Tibble

    Examples
    --------
    >>> tp.from_polars(df)
    """
    df.__class__ = Tibble
    return df

def from_pandas(df):
    """
    Convert from pandas DataFrame to Tibble

    Parameters
    ----------
    df : DataFrame
        pd.DataFrame to convert to a Tibble

    Examples
    --------
    >>> tp.from_pandas(df)
    """
    return from_polars(pl.from_pandas(df))

class Tibble(pl.DataFrame):
    def __init__(self, *args, **kwargs):
        args = _args_as_list(args)
        if len(args) == 0:
            data = kwargs
        else:
            data = args[0]
        super().__init__(data)
    
    def __repr__(self) -> str:
        df = self.to_polars()
        return df.__str__()

    def __getattribute__(self, attr):
        """Prevent access to polars attributes"""
        if attr in _polars_methods:
            raise AttributeError
        return pl.DataFrame.__getattribute__(self, attr)

    def __dir__(self):
        methods = [
            'arrange', 'bind_cols', 'bind_rows', 'colnames', 'clone',
            'distinct', 'drop', 'head', 'fill', 'filter',
            'mutate', 'pivot_longer', 'pivot_wider', 'pull',
            'relocate', 'rename', 'select', 'slice',
            'slice_head', 'slice_tail', 'summarize', 'tail',
            'to_pandas', 'to_polars'
        ]
        return methods

    def arrange(self, *args, desc: bool = False):
        """
        Arrange/sort rows

        Parameters
        ----------
        *args : str
            Columns to sort by
        desc : bool
            Should columns be ordered in descending order

        Examples
        --------
        >>> df = tp.Tibble({'x': ['a', 'a', 'b'], 'y': range(3)})
        >>> # Arrange in ascending order
        >>> df.arrange('x', 'y')
        ...
        >>> # Arrange some columns descending
        >>> df.arrange('x', 'y', desc = [True, False])
        """
        exprs = _args_as_list(args)
        return super().sort(exprs, reverse = desc).pipe(from_polars)

    def bind_cols(self, *args):
        """
        Bind data frames by columns

        Parameters
        ----------
        df : Tibble
            Data frame to bind

        Examples
        --------
        >>> df1 = tp.Tibble({'x': ['a', 'a', 'b'], 'y': range(3)})
        >>> df2 = tp.Tibble({'a': ['c', 'c', 'c'], 'b': range(4, 7)})
        >>> df1.bind_cols(df2)
        """
        frames = _args_as_list(args)
        out = self
        for frame in frames:
            out = super(Tibble, out).hstack(frame).pipe(from_polars)
        return out
    
    def bind_rows(self, *args):
        """
        Bind data frames by row

        Parameters
        ----------
        *args : Union[Tibble, typ.List[Tibble]]
            Data frames to bind by row

        Examples
        --------
        >>> df1 = tp.Tibble({'x': ['a', 'a', 'b'], 'y': range(3)})
        >>> df2 = tp.Tibble({'x': ['c', 'c', 'c'], 'y': range(4, 7)})
        >>> df1.bind_rows(df2)
        """
        frames = _args_as_list(args)
        out = pl.concat([self, *frames])
        return out.pipe(from_polars)

    def clone(self):
        """Very cheap deep clone"""
        return super().clone().pipe(from_polars)

    def distinct(self, *args):
        """
        Select distinct/unique rows

        Parameters
        ----------
        *args : Union[str, Expr]
            Columns to find distinct/unique rows

        Examples
        --------
        >>> df = tp.tibble({'a': range(3), 'b': ['a', 'a', 'b']})
        >>> df.distinct()
        >>> df.distinct('b')
        """
        # TODO: Create for series
        args = _args_as_list(args)

        if len(args) == 0:
            df = super().drop_duplicates()
        else:
            df = super().select(args).drop_duplicates()
        
        return df.pipe(from_polars)

    def drop(self, *args):
        """
        Drop unwanted columns

        Parameters
        ----------
        *args : str
            Columns to drop

        Examples
        --------
        >>> df.drop('x', 'y')
        """
        args = _args_as_list(args)
        return super().drop(args).pipe(from_polars)

    def drop_null(self, *args):
        """
        Drop rows containing missing values

        Parameters
        ----------
        *args : str
            Columns to drop nulls from (defaults to all)

        Examples
        --------
        >>> df = tp.Tibble(x = [1, None, 3], y = [None, 'b', 'c'], z = range(3)}
        >>> df.drop_null()
        >>> df.drop_null('x', 'y')
        """
        args = _args_as_list(args)
        if len(args) == 0:
            out = super().drop_nulls()
        else:
            out = super().drop_nulls(args)
        return out.pipe(from_polars)
    
    def head(self, n = 5, *args, groupby = None):
        """Alias for `.slice_head()`"""
        return self.slice_tail(n, groupby = groupby)

    def fill(self, *args, direction: str = 'down', groupby = None):
        """
        Fill in missing values with previous or next value

        Parameters
        ----------
        *args : str
            Columns to fill
        direction : str
            Direction to fill. One of ['down', 'up', 'downup', 'updown']
        groupby : Union[str, Expr, typ.List[str], typ.List[Expr]]
            Columns to group by

        Examples
        --------
        >>> df = tp.Tibble({'a': [1, None, 3, 4, 5],
        ...                 'b': [None, 2, None, None, 5],
        ...                 'groups': ['a', 'a', 'a', 'b', 'b']})
        >>> df.fill('a', 'b')
        >>> df.fill('a', 'b', groupby = 'groups')
        >>> df.fill('a', 'b', direction = 'downup')
        """
        args = _args_as_list(args)
        if len(args) == 0: return self
        args = _col_exprs(args)
        options = {'down': 'forward', 'up': 'backward'}
        if direction in ['down', 'up']:
            direction = options[direction]
            exprs = [arg.fill_null(direction) for arg in args]
        elif direction == 'downup':
            exprs = [arg.fill_null('forward').fill_null('backward') for arg in args]
        elif direction == 'updown':
            exprs = [arg.fill_null('backward').fill_null('forward') for arg in args]
        else:
            raise ValueError("direction must be one of down, up, downup, or updown")

        return self.mutate(*exprs, groupby = groupby)

    def filter(self, *args,
               groupby: Union[str, Expr, typ.List[str], typ.List[Expr]] = None):
        """
        Filter rows on one or more conditions

        Parameters
        ----------
        *args : Expr
            Conditions to filter by
        groupby : Union[str, Expr, typ.List[str], typ.List[Expr]]
            Columns to group by

        Examples
        --------
        >>> df = tp.Tibble({'a': range(3), 'b': ['a', 'a', 'b']})
        >>> df.filter(col('a') < 2, col('c') == 'a')
        >>> df.filter((col('a') < 2) & (col('c') == 'a'))
        >>> df.filter(col('a') <= col('a').mean(),
        ...           groupby = 'b')
        """
        args = _args_as_list(args)
        exprs = ft.reduce(lambda a, b: a & b, args)

        if _no_groupby(groupby):
            out = super().filter(exprs)
        else:
            out = super().groupby(groupby).apply(lambda x: x.filter(exprs))
        
        return out.pipe(from_polars)

    def mutate(self, *args,
               groupby: Union[str, Expr, typ.List[str], typ.List[Expr]] = None,
               **kwargs):
        """
        Add or modify columns

        Parameters
        ----------
        *args : Expr
            Column expressions to add or modify
        groupby : Union[str, Expr, typ.List[str], typ.List[Expr]]
            Columns to group by
        **kwargs : Expr
            Column expressions to add or modify

        Examples
        --------
        >>> df = tp.Tibble({'a': range(3), 'b': range(3)})
        >>> df.mutate(double_a = col('a') * 2,
        ...           a_plus_b = col('a') + col('b'))
        >>> df.mutate((col(['a', 'b]) * 2).prefix('double_'),
        ...           a_plus_b = col('a') + col('b'))
        """
        exprs = _args_as_list(args) + _kwargs_as_exprs(kwargs)
        if _no_groupby(groupby):
            out = super(Tibble, self).with_columns(exprs)
        else:
            out = super(Tibble, self).groupby(groupby).apply(lambda x: x.with_columns(exprs))
        
        return out.pipe(from_polars)

    @property
    def names(self):
        """Get column names"""
        return super().columns

    @property
    def ncol(self):
        """Get number of columns"""
        return super().shape[1]

    @property
    def nrow(self):
        """Get number of rows"""
        return super().shape[0]

    def pivot_longer(self,
                     cols: Expr = pl.all(),
                     names_to: str = "name",
                     values_to: str = "value"):
        """
        Pivot data from wide to long

        Parameters
        ----------
        cols : Expr
            List of the columns to pivot. Defaults to all columns.
        names_to : str
            Name of the new "names" column.
        values_to: str
            Name of the new "values" column

        Examples
        --------
        >>> df = tp.Tibble({'id': ['id1', 'id2'], 'a': [1, 2], 'b': [1, 2]})
        >>> df.pivot_longer(cols = ['a', 'b'])
        >>> df.pivot_longer(cols = ['a', 'b'], names_to = 'stuff', values_to = 'things')
        """
        df_cols = pl.Series(self.names)
        value_vars = pl.Series(self.select(cols).names)
        id_vars = df_cols[~df_cols.is_in(value_vars)]
        out = super().melt(id_vars, value_vars).rename({'variable': names_to, 'value': values_to})
        return out.pipe(from_polars)

    def pivot_wider(self,
                    names_from: str = 'name',
                    values_from: str = 'value',
                    id_cols: Union[str, typ.List[str]] = None,
                    values_fn: str = 'first', 
                    values_fill: Union[str, int, float] = None):
        """
        Pivot data from long to wide

        Parameters
        ----------
        names_from : str
            Column to get the new column names from.
        values_from : str
            Column to get the new column values from
        id_cols : str
            A set of columns that uniquely identifies each observation.
            Defaults to all columns in the data table except for the columns specified in
            `names_from` and `values_from`.
        values_fn : str
            Function for how multiple entries per group should be dealt with.
        values_fill : str
            If values are missing/null, what value should be filled in.
            Can use: "backward", "forward", "mean", "min", "max", "zero", "one" or an expression

        Examples
        --------
        >>> df = tp.Tibble({'id': [1, 1], 'variable': ['a', 'b'], 'value': [1, 2]})
        >>> df.pivot_wider(names_from = 'variable', values_from = 'value')
        """
        if id_cols == None:
            df_cols = pl.Series(self.names)
            from_cols = pl.Series(self.select(names_from, values_from).names)
            id_cols = df_cols[~df_cols.is_in(from_cols)]

        no_id = len(id_cols) == 0

        if no_id:
            id_cols = '_id'
            self = self.mutate(_id = pl.lit(1))
        
        fn_options = {
            'first': pl.eager.frame.PivotOps.first,
            'count': pl.eager.frame.PivotOps.count,
            'mean': pl.eager.frame.PivotOps.mean,
            'sum': pl.eager.frame.PivotOps.sum,
        }

        values_fn = fn_options[values_fn]

        out = values_fn(super(Tibble, self).groupby(id_cols).pivot(names_from, values_from))

        if values_fill != None: out = out.fill_null(values_fill)

        if no_id: out = out.drop('_id')

        return out.pipe(from_polars)

    def pull(self, var: str = None):
        """
        Extract a column as a series

        Parameters
        ----------
        var : str
            Name of the column to extract. Defaults to the last column.

        Examples
        --------
        >>> df = tp.Tibble({'a': range(3), 'b': range(3))
        >>> df.pull('a')
        """
        if var == None:
            var = self.names[-1]
        
        return super().get_column(var)
    
    def relocate(self, *args, before: str = None, after: str = None):
        """
        Move a column or columns to a new position

        Parameters
        ----------
        *args : Union[str, Expr]
            Columns to move

        Examples
        --------
        >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
        >>> df.relocate('a', before = 'c')
        >>> df.relocate('b', after = 'c')
        """
        move_cols = _args_as_list(args)
        push_length = len(move_cols)
        col_dict = dict((column.name, index) for index, column in enumerate(self)) 
        
        if (before == None) & (after == None) & (push_length == 0):
            return self
        elif (before != None) & (after != None):
            raise ValueError("Cannot provide both before and after")
        elif before != None:
            anchor, push_cols = col_dict[before], (-1 - push_length)
            [col_dict.update({key : push_cols + val}) for key, val in col_dict.items() if val < anchor]
            [col_dict.update({key : anchor - (index + 1)}) for index, key in enumerate(reversed(move_cols))]
        elif after != None:
            anchor, push_cols = col_dict[after], (1 + push_length)
            [col_dict.update({key : push_cols + val}) for key, val in col_dict.items() if val > anchor]
            [col_dict.update({key : anchor + (index + 1)}) for index, key in enumerate(move_cols)]

        ordered_cols = dict(sorted(col_dict.items(), key = lambda x:x[1])).keys()
        return self.select(list(ordered_cols))
   
    def rename(self, *args, **kwargs):
        """
        Rename columns

        Parameters
        ----------
        *args : Dict[str, str]
            Dictionary mapping of new names

        Examples
        --------
        >>> df = tp.Tibble({'x': range(3), 't': range(3), 'z': ['a', 'a', 'b']})
        >>> df.rename(new_x = 'x') # dplyr interface
        >>> df.rename({'x': 'new_x'}) # pandas interface
        """
        args = _args_as_list(args)
        if len(args) > 0:
            if isinstance(args[0], dict):
                mapping = args[0]
            else:
                args = pl.Series(args)
                len_args = len(args)
                if (len_args % 2) == 1:
                    raise ValueError("Need matching new_name/old_name pairs when using args")
                even_bool = pl.Series([True, False] * int(len_args/2))
                new_names = args[even_bool]
                old_names = args[~even_bool]
                mapping = {key:value for key, value in zip(old_names, new_names)}
        else:
            mapping = {value:key for key, value in kwargs.items()}
        return super().rename(mapping).pipe(from_polars)
    
    def select(self, *args):
        """
        Select or drop columns

        Parameters
        ----------
        *args : Union[str, Expr]
            Columns to select

        Examples
        --------
        >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
        >>> df.select('a', 'b')
        >>> df.select(col('a'), col('b'))
        """
        args = _args_as_list(args)
        return super().select(args).pipe(from_polars)

    def slice(self, *args, groupby = None):
        """
        Grab rows from a data frame

        Parameters
        ----------
        *args : Union[int, typ.List[int]]
            Rows to grab
        groupby : Union[str, Expr, typ.List[str], typ.List[Expr]]
            Columns to group by

        Examples
        --------
        >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
        >>> df.slice(0, 1)
        >>> df.slice(0, groupby = 'c')
        """
        rows = _args_as_list(args)
        if _no_groupby(groupby):
            df = super(Tibble, self).select(all().take(rows))
        else:
            df = super(Tibble, self).groupby(groupby).apply(lambda x: x.select(all().take(rows)))
        return df.pipe(from_polars)

    def slice_head(self, n: int = 5, *args, groupby = None):
        """
        Grab top rows from a data frame

        Parameters
        ----------
        n : int
            Number of rows to grab
        *args :
            Currently unused
        groupby : Union[str, Expr, typ.List[str], typ.List[Expr]]
            Columns to group by

        Examples
        --------
        >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
        >>> df.slice_head(2)
        >>> df.slice_head(1, groupby = 'c')
        """
        args = _args_as_list(args)
        col_order = self.names
        if _no_groupby(groupby):
            df = super(Tibble, self).head(n)
        else:
            df = super(Tibble, self).groupby(groupby).head(n)
        return df.pipe(from_polars).select(col_order)

    def slice_tail(self, n: int = 5, *args, groupby = None):
        """
        Grab bottom rows from a data frame

        Parameters
        ----------
        n : int
            Number of rows to grab
        *args :
            Currently unused
        groupby : Union[str, Expr, typ.List[str], typ.List[Expr]]
            Columns to group by

        Examples
        --------
        >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
        >>> df.slice_tail(2)
        >>> df.slice_tail(1, groupby = 'c')
        """
        args = _args_as_list(args)
        col_order = self.names
        if _no_groupby(groupby):
            df = super(Tibble, self).tail(n)
        else:
            df = super(Tibble, self).groupby(groupby).tail(n)
        return df.pipe(from_polars).select(col_order)
    
    def summarise(self, *args,
                  groupby: Union[str, Expr, typ.List[str], typ.List[Expr]] = None,
                  **kwargs):
        """Alias for .summarize()"""
        return self.summarize(*args, groupby = groupby, **kwargs)
    
    def summarize(self, *args,
                  groupby: Union[str, Expr, typ.List[str], typ.List[Expr]] = None,
                  **kwargs):
        """
        Aggregate data with summary statistics

        Parameters
        ----------
        *args : Expr
            Column expressions to add or modify
        groupby : Union[str, Expr, typ.List[str], typ.List[Expr]]
            Columns to group by
        **kwargs : Expr
            Column expressions to add or modify

        Examples
        --------
        >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
        >>> df.summarize(avg_a = col('a').mean())
        >>> df.summarize(avg_a = col('a').mean(),
        ...              groupby = 'c')
        >>> df.summarize(avg_a = col('a').mean(),
        ...              max_b = col('b').max())
        """
        exprs = _args_as_list(args) + _kwargs_as_exprs(kwargs)

        if _no_groupby(groupby):
            out = super(Tibble, self).select(exprs)
        else:
            out = super(Tibble, self).groupby(groupby).agg(exprs)
        
        return out.pipe(from_polars)

    def tail(self, n = 5, *args, groupby = None):
        """Alias for `.slice_tail()`"""
        return self.slice_tail(n, groupby = groupby)

    def to_pandas(self):
        """
        Convert to a polars DataFrame

        Examples
        --------
        >>> df.to_pandas()
        """
        return super().to_pandas()

    def to_polars(self):
        """
        Convert to a polars DataFrame

        Examples
        --------
        >>> df.to_polars()
        """
        self.__class__ = pl.DataFrame
        return self

_allowed_methods = [
    'dtypes', 'frame_equal',
    'get_columns', 'lazy', 'pipe'
]

_polars_methods = [
    'apply',
    'columns',
    # 'describe',
    'downsample',
    'drop_duplicates',
    'explode',
    'fill_nan',
    'fill_null',
    'find_idx_by_name',
    'fold',
    'get_column',
    'groupby',
    'hash_rows',
    'height',
    'hstack',
    'insert_at_idx',
    'interpolate',
    'is_duplicated',
    'is_unique',
    'join',
    'limit',
    'max',
    'mean',
    'median',
    'melt',
    'min',
    'n_chunks',
    'null_count',
    'quantile',
    'rechunk',
    'replace',
    'replace_at_idx',
    'row',
    'rows'
    'sample',
    'select_at_idx',
    'shape',
    'shift',
    'shift_and_fill',
    'shrink_to_fit',
    'sort',
    'std',
    'sum',
    'to_arrow',
    'to_dict',
    'to_dicts',
    'to_dummies',
    'to_ipc',
    'to_json',
    'to_numpy'
    'to_pandas'
    'to_parquet',
    'transpose',
    'var',
    'width',
    'with_column',
    'with_columns',
    'with_column_renamed',
    'with_columns'
]