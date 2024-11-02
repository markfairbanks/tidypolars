import polars as pl
import functools as ft
from .utils import (
    _as_list,
    _col_expr,
    _col_exprs,
    _is_expr,
    _is_string,
    _kwargs_as_exprs,
    _mutate_cols,
    _uses_by
)
from .stringr import str_c
import copy
from .reexports import *
from .tidyselect import everything
from operator import not_

__all__ = [
    "as_tibble",
    "is_tibble",
    "tibble",
    "desc",
    "from_pandas", "from_polars"
]

class tibble(pl.DataFrame):
    """
    A data frame object that provides methods familiar to R tidyverse users.
    """
    def __init__(self, _data = None, **kwargs):
        if len(kwargs) > 0:
            _data = kwargs
        elif not_(isinstance(_data, dict)):
            raise ValueError("_data must be a dictionary or kwargs must be used")
        super().__init__(_data)

    def __dir__(self):
        _tidypolars_methods = [
            'arrange', 'as_dict', 'as_pandas', 'as_polars',
            'bind_cols', 'bind_rows', 'colnames', 'clone', 'count',
            'distinct', 'drop', 'drop_null', 'head', 'fill', 'filter',
            'glimpse',
            'inner_join', 'left_join', 'mutate', 'names', 'nrow', 'ncol',
            'full_join', 'pivot_longer', 'pivot_wider',
            'print',
            'pull', 'relocate', 'rename', 'replace_null', 'select',
            'separate', 'set_names',
            'slice', 'slice_head', 'slice_tail', 'summarize', 'tail',
            'write_csv', 'write_parquet'
        ]
        return _tidypolars_methods
    
    def __repr__(self):
        """Printing method"""
        df = self.as_polars()
        return df.__str__()
    
    def _repr_html_(self):
        """
        Printing method for jupyter

        Output rows and columns can be modified by setting the following ENVIRONMENT variables:

        * POLARS_FMT_MAX_COLS: set the number of columns

        * POLARS_FMT_MAX_ROWS: set the number of rows
        """
        df = self.as_polars()
        return df._repr_html_()

    def __copy__(self):
        # Shallow copy
        # See: https://stackoverflow.com/a/51043609/13254470
        obj = type(self).__new__(self.__class__)
        obj.__dict__.update(self.__dict__)
        return obj

    def __str__(self):
        """Printing method"""
        df = self.as_polars()
        return df.__str__()

    def __getattribute__(self, attr):
        if attr in _polars_methods:
            raise AttributeError
        return pl.DataFrame.__getattribute__(self, attr)
    
    def __getitem__(self, col):
        return self.pull(col)

    def arrange(self, *args):
        """
        Arrange/sort rows

        Parameters
        ----------
        *args : str
            Columns to sort by

        Examples
        --------
        >>> df = tp.tibble({'x': ['a', 'a', 'b'], 'y': range(3)})
        >>> # Arrange in ascending order
        >>> df.arrange('x', 'y')
        ...
        >>> # Arrange some columns descending
        >>> df.arrange(tp.desc('x'), 'y')
        """
        exprs = _as_list(args)
        desc = [True if isinstance(expr, DescCol) else False for expr in exprs]
        return super().sort(exprs, descending = desc).pipe(from_polars)
    
    def as_dict(self, *, as_series = True):
        """
        Aggregate data with summary statistics

        Parameters
        ----------
        as_series : bool
            If True - returns the dict values as Series
            If False - returns the dict values as lists

        Examples
        --------
        >>> df.to_dict()
        >>> df.to_dict(as_series = False)
        """
        return super().to_dict(as_series = as_series)

    def as_pandas(self):
        """
        Convert to a pandas DataFrame

        Examples
        --------
        >>> df.as_pandas()
        """
        return self.as_polars().to_pandas()

    def as_polars(self):
        """
        Convert to a polars DataFrame

        Examples
        --------
        >>> df.as_polars()
        """
        self = copy.copy(self)
        self.__class__ = pl.DataFrame
        return self

    def bind_cols(self, *args):
        """
        Bind data frames by columns

        Parameters
        ----------
        df : tibble
            Data frame to bind

        Examples
        --------
        >>> df1 = tp.tibble({'x': ['a', 'a', 'b'], 'y': range(3)})
        >>> df2 = tp.tibble({'a': ['c', 'c', 'c'], 'b': range(4, 7)})
        >>> df1.bind_cols(df2)
        """
        frames = _as_list(args)
        out = self.as_polars()
        for frame in frames:
            out = out.hstack(frame)
        return out.pipe(from_polars)
    
    def bind_rows(self, *args):
        """
        Bind data frames by row

        Parameters
        ----------
        *args : tibble, list
            Data frames to bind by row

        Examples
        --------
        >>> df1 = tp.tibble({'x': ['a', 'a', 'b'], 'y': range(3)})
        >>> df2 = tp.tibble({'x': ['c', 'c', 'c'], 'y': range(4, 7)})
        >>> df1.bind_rows(df2)
        """
        frames = _as_list(args)
        out = pl.concat([self, *frames], how = "diagonal")
        return out.pipe(from_polars)

    def clone(self):
        """Very cheap deep clone"""
        return super().clone().pipe(from_polars)

    def count(self, *args, sort = False, name = 'n'):
        """
        Returns row counts of the dataset. 
        If bare column names are provided, count() returns counts by group.

        Parameters
        ----------
        *args : str, Expr
            Columns to group by
        sort : bool
            Should columns be ordered in descending order by count
        name : str
            The name of the new column in the output. If omitted, it will default to "n".

        Examples
        --------
        >>> df = tp.tibble({'a': range(3), 'b': ['a', 'a', 'b']})
        >>> df.count()
        >>> df.count('b')
        """
        args = _as_list(args)
        
        out = self.summarize(pl.len().alias(name), _by = args)

        if sort == True:
            out = out.arrange(desc(name))

        return out

    def distinct(self, *args):
        """
        Select distinct/unique rows

        Parameters
        ----------
        *args : str, Expr
            Columns to find distinct/unique rows

        Examples
        --------
        >>> df = tp.tibble({'a': range(3), 'b': ['a', 'a', 'b']})
        >>> df.distinct()
        >>> df.distinct('b')
        """
        args = _as_list(args)
        if len(args) == 0:
            df = super().unique()
        else:
            df = super().select(args).unique()
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
        args = _as_list(args)
        drop_cols = self.select(args).names
        return super().drop(drop_cols).pipe(from_polars)

    def drop_null(self, *args):
        """
        Drop rows containing missing values

        Parameters
        ----------
        *args : str
            Columns to drop nulls from (defaults to all)

        Examples
        --------
        >>> df = tp.tibble(x = [1, None, 3], y = [None, 'b', 'c'], z = range(3)}
        >>> df.drop_null()
        >>> df.drop_null('x', 'y')
        """
        args = _as_list(args)
        if len(args) == 0:
            out = super().drop_nulls()
        else:
            out = super().drop_nulls(args)
        return out.pipe(from_polars)
    
    def equals(self, other, null_equal = True):
        """Check if two tibbles are equal"""
        df = self.as_polars()
        other = other.as_polars()
        return df.equals(other, null_equal = null_equal)
    
    def glimpse(self):
        """
        Return a dense preview of the DataFrame.
        
        The formatting shows one line per column so that wide dataframes display cleanly. 
        Each line shows the column name, the data type, and the first few values.
        """
        return self.as_polars().glimpse()

    def fill(self, *args, direction = 'down', _by = None):
        """
        Fill in missing values with previous or next value

        Parameters
        ----------
        *args : str
            Columns to fill
        direction : str
            Direction to fill. One of ['down', 'up', 'downup', 'updown']
        by : str, list
            Columns to group by

        Examples
        --------
        >>> df = tp.tibble({'a': [1, None, 3, 4, 5],
        ...                 'b': [None, 2, None, None, 5],
        ...                 'groups': ['a', 'a', 'a', 'b', 'b']})
        >>> df.fill('a', 'b')
        >>> df.fill('a', 'b', by = 'groups')
        >>> df.fill('a', 'b', direction = 'downup')
        """
        args = _as_list(args)
        if len(args) == 0: return self
        args = _col_exprs(args)
        options = {'down': 'forward', 'up': 'backward'}
        if direction in ['down', 'up']:
            direction = options[direction]
            exprs = [arg.fill_null(strategy = direction) for arg in args]
        elif direction == 'downup':
            exprs = [
                arg.fill_null(strategy = 'forward').fill_null(strategy = 'backward')
                for arg in args
            ]
        elif direction == 'updown':
            exprs = [
                arg.fill_null(strategy = 'backward')
                .fill_null(strategy = 'forward')
                for arg in args
            ]
        else:
            raise ValueError("direction must be one of down, up, downup, or updown")

        return self.mutate(*exprs, _by = _by)

    def filter(self, *args,
               _by = None):
        """
        Filter rows on one or more conditions

        Parameters
        ----------
        *args : Expr
            Conditions to filter by
        by : str, list
            Columns to group by

        Examples
        --------
        >>> df = tp.tibble({'a': range(3), 'b': ['a', 'a', 'b']})
        >>> df.filter(col('a') < 2, col('b') == 'a')
        >>> df.filter((col('a') < 2) & (col('b') == 'a'))
        >>> df.filter(col('a') <= tp.mean(col('a')), by = 'b')
        """
        args = _as_list(args)
        exprs = ft.reduce(lambda a, b: a & b, args)

        if _uses_by(_by):
            out = super().group_by(_by).map_groups(lambda x: x.filter(exprs))
        else:
            out = super().filter(exprs)
        
        return out.pipe(from_polars)
    
    def full_join(self, df, left_on = None, right_on = None, on = None, suffix: str = '_right'):
        """
        Perform an full join

        Parameters
        ----------
        df : tibble
            Lazy DataFrame to join with.
        left_on : str, list
            Join column(s) of the left DataFrame.
        right_on : str, list
            Join column(s) of the right DataFrame.
        on: str, list
            Join column(s) of both DataFrames. If set, `left_on` and `right_on` should be None.
        suffix : str
            Suffix to append to columns with a duplicate name.

        Examples
        --------
        >>> df1.full_join(df2)
        >>> df1.full_join(df2, on = 'x')
        >>> df1.full_join(df2, left_on = 'left_x', right_on = 'x')
        """
        if (left_on == None) & (right_on == None) & (on == None):
            on = list(set(self.names) & set(df.names))
        out = super().join(df, on, "full", left_on = left_on, right_on = right_on, suffix = suffix, coalesce = True)
        return out.pipe(from_polars)
    
    def head(self, n = 5, *, _by = None):
        """Alias for `.slice_head()`"""
        return self.slice_head(n, _by = _by)

    def inner_join(self, df, left_on = None, right_on = None, on = None, suffix = '_right'):
        """
        Perform an inner join

        Parameters
        ----------
        df : tibble
            Lazy DataFrame to join with.
        left_on : str, list
            Join column(s) of the left DataFrame.
        right_on : str, list
            Join column(s) of the right DataFrame.
        on: str, list
            Join column(s) of both DataFrames. If set, `left_on` and `right_on` should be None.
        suffix : str
            Suffix to append to columns with a duplicate name.

        Examples
        --------
        >>> df1.inner_join(df2)
        >>> df1.inner_join(df2, on = 'x')
        >>> df1.inner_join(df2, left_on = 'left_x', right_on = 'x')
        """
        if (left_on == None) & (right_on == None) & (on == None):
            on = list(set(self.names) & set(df.names))
        return super().join(df, on, 'inner', left_on = left_on, right_on= right_on, suffix= suffix).pipe(from_polars)

    def left_join(self, df, left_on = None, right_on = None, on = None, suffix = '_right'):
        """
        Perform a left join

        Parameters
        ----------
        df : tibble
            Lazy DataFrame to join with.
        left_on : str, list
            Join column(s) of the left DataFrame.
        right_on : str, list
            Join column(s) of the right DataFrame.
        on: str, list
            Join column(s) of both DataFrames. If set, `left_on` and `right_on` should be None.
        suffix : str
            Suffix to append to columns with a duplicate name.

        Examples
        --------
        >>> df1.left_join(df2)
        >>> df1.left_join(df2, on = 'x')
        >>> df1.left_join(df2, left_on = 'left_x', right_on = 'x')
        """
        if (left_on == None) & (right_on == None) & (on == None):
            on = list(set(self.names) & set(df.names))
        return super().join(df, on, 'left',  left_on = left_on, right_on= right_on, suffix= suffix).pipe(from_polars)

    def mutate(self, *args,
               _by = None,
               **kwargs):
        """
        Add or modify columns

        Parameters
        ----------
        *args : Expr
            Column expressions to add or modify
        by : str, list
            Columns to group by
        **kwargs : Expr
            Column expressions to add or modify

        Examples
        --------
        >>> df = tp.tibble({'a': range(3), 'b': range(3), c = ['a', 'a', 'b']})
        >>> df.mutate(double_a = col('a') * 2,
        ...           a_plus_b = col('a') + col('b'))
        >>> df.mutate(row_num = row_number(), by = 'c')
        """
        exprs = _as_list(args) + _kwargs_as_exprs(kwargs)

        out = self.as_polars()

        if _uses_by(_by):
            out = out.group_by(_by).map_groups(lambda x: _mutate_cols(x, exprs))
        else:
            out = _mutate_cols(out, exprs)
            
        return out.pipe(from_polars)

    def pivot_longer(self,
                     cols = everything(),
                     names_to = "name",
                     values_to = "value"):
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
        >>> df = tp.tibble({'id': ['id1', 'id2'], 'a': [1, 2], 'b': [1, 2]})
        >>> df.pivot_longer(cols = ['a', 'b'])
        >>> df.pivot_longer(cols = ['a', 'b'], names_to = 'stuff', values_to = 'things')
        """
        df_cols = pl.Series(self.names)
        value_vars = self.select(cols).names
        id_vars = df_cols.filter(df_cols.is_in(value_vars).not_()).to_list()
        out = super().unpivot(index = id_vars, on = value_vars, variable_name = names_to, value_name = values_to)
        return out.pipe(from_polars)

    def pivot_wider(self,
                    names_from = 'name',
                    values_from = 'value',
                    id_cols = None,
                    values_fn = 'first', 
                    values_fill = None):
        """
        Pivot data from long to wide

        Parameters
        ----------
        names_from : str
            Column to get the new column names from.
        values_from : str
            Column to get the new column values from
        id_cols : str, list
            A set of columns that uniquely identifies each observation.
            Defaults to all columns in the data table except for the columns specified in
            `names_from` and `values_from`.
        values_fn : str
            Function for how multiple entries per group should be dealt with.
            Any of 'first', 'count', 'sum', 'max', 'min', 'mean', 'median', 'last'
        values_fill : str
            If values are missing/null, what value should be filled in.
            Can use: "backward", "forward", "mean", "min", "max", "zero", "one"

        Examples
        --------
        >>> df = tp.tibble({'id': [1, 1], 'variable': ['a', 'b'], 'value': [1, 2]})
        >>> df.pivot_wider(names_from = 'variable', values_from = 'value')
        """
        if id_cols == None:
            df_cols = pl.Series(self.names)
            from_cols = pl.Series(self.select(names_from, values_from).names)
            id_cols = df_cols.filter(df_cols.is_in(from_cols).not_()).to_list()

        no_id = len(id_cols) == 0

        if no_id:
            id_cols = '_id'
            self = self.mutate(_id = pl.lit(1))

        out = (
            super()
            .pivot(values = values_from, index = id_cols, on = names_from, aggregate_function = values_fn)
            .pipe(from_polars)
        )

        if values_fill != None:
            new_cols = pl.Series(out.names)
            new_cols = new_cols.filter(~new_cols.is_in(id_cols))
            fill_exprs = [col(new_col).fill_null(values_fill) for new_col in new_cols]
            out = out.mutate(*fill_exprs)

        if no_id: out = out.drop('_id')

        return out
    
    def print(self):
        self.pipe(print)

    def pull(self, var = None):
        """
        Extract a column as a series

        Parameters
        ----------
        var : str
            Name of the column to extract. Defaults to the last column.

        Examples
        --------
        >>> df = tp.tibble({'a': range(3), 'b': range(3))
        >>> df.pull('a')
        """
        if var == None:
            var = self.names[-1]
        
        return super().get_column(var)
    
    def relocate(self, *args, _before = None, _after = None):
        """
        Move a column or columns to a new position

        Parameters
        ----------
        *args : str, Expr
            Columns to move

        Examples
        --------
        >>> df = tp.tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
        >>> df.relocate('a', before = 'c')
        >>> df.relocate('b', after = 'c')
        """
        cols_all = pl.Series(self.names)
        locs_all = pl.Series(range(len(cols_all)))
        locs_dict = {k:v for k,v in zip(cols_all, locs_all)}
        locs_df = pl.DataFrame(locs_dict, orient = "row")

        cols_relocate = _as_list(args)
        locs_relocate = pl.Series(locs_df.select(cols_relocate).row(0))

        if (len(locs_relocate) == 0):
            return self

        uses_before = _is_expr(_before) | _is_string(_before)
        uses_after = _is_expr(_after) | _is_string(_after)

        if (uses_before & uses_after):
            raise ValueError("Cannot provide both before and after")
        elif (not_(uses_before) & not_(uses_after)):
            _before = cols_all[0]
            uses_before = True

        if uses_before:
            _before = locs_df.select(_before).get_column(_before)
            locs_start = locs_all.filter(locs_all < _before)
        else:
            _after = locs_df.select(_after).get_column(_after)
            locs_start = locs_all.filter(locs_all <= _after)

        locs_start = locs_start.filter(~locs_start.is_in(locs_relocate))
        final_order = pl.concat([locs_start, locs_relocate, locs_all]).unique(maintain_order = True)
        final_order = cols_all[final_order].to_list()

        return self.select(final_order)
   
    def rename(self, _mapping = None, **kwargs):
        """
        Rename columns

        Parameters
        ----------
        _mapping : dict
            Dictionary mapping of new names
        **kwargs : str
            key-value pair of new name from old name

        Examples
        --------
        >>> df = tp.tibble({'x': range(3), 't': range(3), 'z': ['a', 'a', 'b']})
        >>> df.rename(new_x = 'x') # dplyr interface
        >>> df.rename({'x': 'new_x'}) # pandas interface
        """
        if _mapping == None:
            _mapping = {value:key for key, value in kwargs.items()} 
        return super().rename(_mapping).pipe(from_polars)

    def replace_null(self, replace = None):
        """
        Replace null values

        Parameters
        ----------
        replace : dict
            Dictionary of column/replacement pairs

        Examples
        --------
        >>> df = tp.tibble(x = [0, None], y = [None, None])
        >>> df.replace_null(dict(x = 1, y = 2))
        """
        if replace == None: return self
        if type(replace) != dict:
            ValueError("replace must be a dictionary of column/replacement pairs")
        replace_exprs = [col(key).fill_null(value) for key, value in replace.items()]
        return self.mutate(*replace_exprs)

    def separate(self, sep_col, into, sep = '_', remove = True):
        """
        Separate a character column into multiple columns

        Parameters
        ----------
        sep_col : str
            Column to split into multiple columns
        into : list
            List of new column names
        sep : str
            Separator to split on. Default to '_'
        remove : bool
            If True removes the input column from the output data frame

        Examples
        --------
        >>> df = tp.tibble(x = ['a_a', 'b_b', 'c_c'])
        >>> df.separate('x', into = ['left', 'right'])
        """
        into_len = len(into) - 1
        sep_df = (
            self
            .as_polars()
            .select(col(sep_col)
                    .str.split_exact(sep, into_len)
                    .alias("_seps")
                    .struct
                    .rename_fields(into))
            .unnest("_seps")
            .pipe(from_polars)
        )
        out = self.bind_cols(sep_df)
        if remove == True:
            out = out.drop(sep_col)
        return out

    def set_names(self, nm = None):
        """
        Change the column names of the data frame

        Parameters
        ----------
        nm : list
            A list of new names for the data frame

        Examples
        --------
        >>> df = tp.tibble(x = range(3), y = range(3))
        >>> df.set_names(['a', 'b'])
        """
        if nm == None: nm = self.names
        nm = _as_list(nm)
        rename_dict = {k:v for k, v in zip(self.names, nm)}
        return self.rename(rename_dict)
    
    def select(self, *args):
        """
        Select or drop columns

        Parameters
        ----------
        *args : str, Expr
            Columns to select

        Examples
        --------
        >>> df = tp.tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
        >>> df.select('a', 'b')
        >>> df.select(col('a'), col('b'))
        """
        args = _as_list(args)
        args = _col_exprs(args)
        return super().select(args).pipe(from_polars)

    def slice(self, *args, _by = None):
        """
        Grab rows from a data frame

        Parameters
        ----------
        *args : int, list
            Rows to grab
        by : str, list
            Columns to group by

        Examples
        --------
        >>> df = tp.tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
        >>> df.slice(0, 1)
        >>> df.slice(0, by = 'c')
        """
        rows = _as_list(args)
        if _uses_by(_by):
            df = super(tibble, self).group_by(_by).map_groups(lambda x: x.select(pl.all().gather(rows)))
        else:
            df = super(tibble, self).select(pl.all().gather(rows))
        return df.pipe(from_polars)

    def slice_head(self, n = 5, *, _by = None):
        """
        Grab top rows from a data frame

        Parameters
        ----------
        n : int
            Number of rows to grab
        by : str, list
            Columns to group by

        Examples
        --------
        >>> df = tp.tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
        >>> df.slice_head(2)
        >>> df.slice_head(1, by = 'c')
        """
        col_order = self.names
        if _uses_by(_by):
            df = super(tibble, self).group_by(_by).head(n)
        else:
            df = super(tibble, self).head(n)
        df = df.select(col_order)
        return df.pipe(from_polars)

    def slice_tail(self, n = 5, *, _by = None):
        """
        Grab bottom rows from a data frame

        Parameters
        ----------
        n : int
            Number of rows to grab
        by : str, list
            Columns to group by

        Examples
        --------
        >>> df = tp.tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
        >>> df.slice_tail(2)
        >>> df.slice_tail(1, by = 'c')
        """
        col_order = self.names
        if _uses_by(_by):
            df = super(tibble, self).group_by(_by).tail(n)
        else:
            df = super(tibble, self).tail(n)
        df = df.select(col_order)
        return df.pipe(from_polars)
    
    def summarise(self, *args,
                  _by = None,
                  **kwargs):
        """Alias for `.summarize()`"""
        return self.summarize(*args, _by = _by, **kwargs)
    
    def summarize(self, *args,
                  _by = None,
                  **kwargs):
        """
        Aggregate data with summary statistics

        Parameters
        ----------
        *args : Expr
            Column expressions to add or modify
        by : str, list
            Columns to group by
        **kwargs : Expr
            Column expressions to add or modify

        Examples
        --------
        >>> df = tp.tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
        >>> df.summarize(avg_a = tp.mean(col('a')))
        >>> df.summarize(avg_a = tp.mean(col('a')),
        ...              by = 'c')
        >>> df.summarize(avg_a = tp.mean(col('a')),
        ...              max_b = tp.max(col('b')))
        """
        exprs = _as_list(args) + _kwargs_as_exprs(kwargs)
        if _uses_by(_by):
            out = super(tibble, self).group_by(_by).agg(exprs)
        else:
            out = super(tibble, self).select(exprs)
        return out.pipe(from_polars)

    def tail(self, n = 5, *, _by = None):
        """Alias for `.slice_tail()`"""
        return self.slice_tail(n, _by = _by)

    def unite(self, col = "_united", unite_cols = [], sep = "_", remove = True):
        """
        Unite multiple columns by pasting strings together

        Parameters
        ----------
        col : str
            Name of the new column
        unite_cols : list
            List of columns to unite
        sep : str
            Separator to use between values
        remove : bool
            If True removes input columns from the data frame

        Examples
        --------
        >>> df = tp.tibble(a = ["a", "a", "a"], b = ["b", "b", "b"], c = range(3))
        >>> df.unite("united_col", unite_cols = ["a", "b"])
        """
        if len(unite_cols) == 0:
            unite_cols = self.names
        else:
            unite_cols = self.select(unite_cols).names
        _before = unite_cols[0]
        unite_cols = _col_exprs(unite_cols)
        out = self.mutate(str_c(*unite_cols, sep = sep).alias(col))
        out = out.relocate(col, _before = _before)
        if remove == True:
            out = out.drop(unite_cols)
        return out
    
    def write_csv(self,
                  file = None,
                  has_headers = True,
                  sep = ','):
        """Write a data frame to a csv"""
        return super().write_csv(file, include_header = has_headers, separator = sep)

    def write_parquet(self,
                      file = str,
                      compression = 'snappy',
                      use_pyarrow = False,
                      **kwargs):
        """Write a data frame to a parquet"""
        return super().write_parquet(file, compression = compression, use_pyarrow = use_pyarrow, **kwargs)
    
    @property
    def names(self):
        """
        Get column names
        
        Examples
        --------
        >>> df.names
        """
        return super().columns

    @property
    def ncol(self):
        """
        Get number of columns
        
        Examples
        --------
        >>> df.ncol
        """
        return super().shape[1]

    @property
    def nrow(self):
        """
        Get number of rows
        
        Examples
        --------
        >>> df.nrow
        """
        return super().shape[0]
    
    @property
    def plot(self):
        """
        Access to polars plotting
        
        Examples
        --------
        >>> df.plot
        """
        return super().plot

def desc(x):
    """Mark a column to order in descending"""
    x = copy.copy(x)
    x = _col_expr(x)
    x.__class__ = DescCol
    return x

class DescCol(pl.Expr):
    pass

def as_tibble(x):
    """
    Convert an object to a tibble

    Parameters
    ----------
    x : [pl.DataFrame, pd.DataFrame, dict]
        Object to convert to a tibble

    Examples
    --------
    >>> tp.as_tibble(polars_df)
    """
    if isinstance(x, pl.DataFrame):
        out = from_polars(x)
    elif isinstance(x, dict):
        out = tibble(x)
    elif is_tibble(x):
        out = x
    else:
        out = pl.from_dataframe(x)
    return out

def is_tibble(x):
    """
    Is an object to a tibble

    Parameters
    ----------
    x : object

    Examples
    --------
    >>> tp.is_tibble(df)
    """
    return isinstance(x, tibble)

def from_polars(df):
    """
    Convert from polars DataFrame to tibble

    Parameters
    ----------
    df : DataFrame
        pl.DataFrame to convert to a tibble

    Examples
    --------
    >>> tp.from_polars(df)
    """
    df = copy.copy(df)
    df.__class__ = tibble
    return df

def from_pandas(df):
    """
    Convert from pandas DataFrame to tibble

    Parameters
    ----------
    df : DataFrame
        pd.DataFrame to convert to a tibble

    Examples
    --------
    >>> tp.from_pandas(df)
    """
    return from_polars(pl.from_pandas(df))

_allowed_methods = [
    'dtypes', 'frame_equal',
    'get_columns', 'lazy', 'pipe'
]

_polars_methods = [
    'apply',
    'columns',
    'describe',
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
    # 'to_arrow',
    # 'to_dict',
    'to_dicts',
    'to_dummies',
    'to_ipc',
    'to_json',
    'to_numpy'
    'to_pandas'
    'to_parquet',
    'transpose',
    'unnest',
    'unpivot',
    'var',
    'width',
    'with_column',
    'with_columns',
    'with_column_renamed',
    'with_columns'
]
