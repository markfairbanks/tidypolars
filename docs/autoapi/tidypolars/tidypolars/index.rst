:py:mod:`tidypolars.tidypolars`
===============================

.. py:module:: tidypolars.tidypolars


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   tidypolars.tidypolars.Tibble



Functions
~~~~~~~~~

.. autoapisummary::

   tidypolars.tidypolars.desc
   tidypolars.tidypolars.from_polars
   tidypolars.tidypolars.from_pandas



.. py:class:: Tibble(*args, **kwargs)

   Bases: :py:obj:`tidypolars.reexports.pl.DataFrame`

   A data frame object that provides methods familiar to R tidyverse users.

   .. py:method:: __repr__(self)

      Return repr(self).


   .. py:method:: __str__(self)

      Return str(self).


   .. py:method:: __getattribute__(self, attr)

      Return getattr(self, name).


   .. py:method:: __dir__(self)

      Default dir() implementation.


   .. py:method:: arrange(self, *args)

      Arrange/sort rows

      :param \*args: Columns to sort by
      :type \*args: str

      .. rubric:: Examples

      >>> df = tp.Tibble({'x': ['a', 'a', 'b'], 'y': range(3)})
      >>> # Arrange in ascending order
      >>> df.arrange('x', 'y')
      ...
      >>> # Arrange some columns descending
      >>> df.arrange(tp.desc('x'), 'y')


   .. py:method:: bind_cols(self, *args)

      Bind data frames by columns

      :param df: Data frame to bind
      :type df: Tibble

      .. rubric:: Examples

      >>> df1 = tp.Tibble({'x': ['a', 'a', 'b'], 'y': range(3)})
      >>> df2 = tp.Tibble({'a': ['c', 'c', 'c'], 'b': range(4, 7)})
      >>> df1.bind_cols(df2)


   .. py:method:: bind_rows(self, *args)

      Bind data frames by row

      :param \*args: Data frames to bind by row
      :type \*args: Tibble, list

      .. rubric:: Examples

      >>> df1 = tp.Tibble({'x': ['a', 'a', 'b'], 'y': range(3)})
      >>> df2 = tp.Tibble({'x': ['c', 'c', 'c'], 'y': range(4, 7)})
      >>> df1.bind_rows(df2)


   .. py:method:: clone(self)

      Very cheap deep clone


   .. py:method:: count(self, *args, sort=False, name='n')

      Returns row counts of the dataset.
      If bare column names are provided, count() returns counts by group.

      :param \*args: Columns to find distinct/unique rows
      :type \*args: str, Expr
      :param sort: Should columns be ordered in descending order by count
      :type sort: bool
      :param name: The name of the new column in the output. If omitted, it will default to N.
      :type name: str

      .. rubric:: Examples

      >>> df = tp.Tibble({'a': range(3), 'b': ['a', 'a', 'b']})
      >>> df.count()
      >>> df.count('b')


   .. py:method:: distinct(self, *args)

      Select distinct/unique rows

      :param \*args: Columns to find distinct/unique rows
      :type \*args: str, Expr

      .. rubric:: Examples

      >>> df = tp.Tibble({'a': range(3), 'b': ['a', 'a', 'b']})
      >>> df.distinct()
      >>> df.distinct('b')


   .. py:method:: drop(self, *args)

      Drop unwanted columns

      :param \*args: Columns to drop
      :type \*args: str

      .. rubric:: Examples

      >>> df.drop('x', 'y')


   .. py:method:: drop_null(self, *args)

      Drop rows containing missing values

      :param \*args: Columns to drop nulls from (defaults to all)
      :type \*args: str

      .. rubric:: Examples

      >>> df = tp.Tibble(x = [1, None, 3], y = [None, 'b', 'c'], z = range(3)}
      >>> df.drop_null()
      >>> df.drop_null('x', 'y')


   .. py:method:: head(self, n=5, *, by=None)

      Alias for `.slice_head()`


   .. py:method:: fill(self, *args, direction='down', by=None)

      Fill in missing values with previous or next value

      :param \*args: Columns to fill
      :type \*args: str
      :param direction: Direction to fill. One of ['down', 'up', 'downup', 'updown']
      :type direction: str
      :param by: Columns to group by
      :type by: str, list

      .. rubric:: Examples

      >>> df = tp.Tibble({'a': [1, None, 3, 4, 5],
      ...                 'b': [None, 2, None, None, 5],
      ...                 'groups': ['a', 'a', 'a', 'b', 'b']})
      >>> df.fill('a', 'b')
      >>> df.fill('a', 'b', by = 'groups')
      >>> df.fill('a', 'b', direction = 'downup')


   .. py:method:: filter(self, *args, by=None)

      Filter rows on one or more conditions

      :param \*args: Conditions to filter by
      :type \*args: Expr
      :param by: Columns to group by
      :type by: str, list

      .. rubric:: Examples

      >>> df = tp.Tibble({'a': range(3), 'b': ['a', 'a', 'b']})
      >>> df.filter(col('a') < 2, col('b') == 'a')
      >>> df.filter((col('a') < 2) & (col('b') == 'a'))
      >>> df.filter(col('a') <= tp.mean(col('a')), by = 'b')


   .. py:method:: frame_equal(self, other, null_equal=True)

      Check if two Tibbles are equal


   .. py:method:: inner_join(self, df, left_on=None, right_on=None, on=None, suffix='_right')

      Perform an inner join

      :param df: Lazy DataFrame to join with.
      :type df: Tibble
      :param left_on: Join column(s) of the left DataFrame.
      :type left_on: str, list
      :param right_on: Join column(s) of the right DataFrame.
      :type right_on: str, list
      :param on: Join column(s) of both DataFrames. If set, `left_on` and `right_on` should be None.
      :type on: str, list
      :param suffix: Suffix to append to columns with a duplicate name.
      :type suffix: str

      .. rubric:: Examples

      df1.inner_join(df2)
      df1.inner_join(df2, on = 'x')
      df1.inner_join(df2, left_on = 'left_x', right_on = 'x')


   .. py:method:: left_join(self, df, left_on=None, right_on=None, on=None, suffix='_right')

      Perform a left join

      :param df: Lazy DataFrame to join with.
      :type df: Tibble
      :param left_on: Join column(s) of the left DataFrame.
      :type left_on: str, list
      :param right_on: Join column(s) of the right DataFrame.
      :type right_on: str, list
      :param on: Join column(s) of both DataFrames. If set, `left_on` and `right_on` should be None.
      :type on: str, list
      :param suffix: Suffix to append to columns with a duplicate name.
      :type suffix: str

      .. rubric:: Examples

      df1.left_join(df2)
      df1.left_join(df2, on = 'x')
      df1.left_join(df2, left_on = 'left_x', right_on = 'x')


   .. py:method:: mutate(self, *args, by=None, **kwargs)

      Add or modify columns

      :param \*args: Column expressions to add or modify
      :type \*args: Expr
      :param by: Columns to group by
      :type by: str, list
      :param \*\*kwargs: Column expressions to add or modify
      :type \*\*kwargs: Expr

      .. rubric:: Examples

      >>> df = tp.Tibble({'a': range(3), 'b': range(3)})
      >>> df.mutate(double_a = col('a') * 2,
      ...           a_plus_b = col('a') + col('b'))
      >>> df.mutate((col(['a', 'b']) * 2).prefix('double_'),
      ...           a_plus_b = col('a') + col('b'))


   .. py:method:: names(self)
      :property:

      Get column names


   .. py:method:: ncol(self)
      :property:

      Get number of columns


   .. py:method:: nrow(self)
      :property:

      Get number of rows


   .. py:method:: full_join(self, df, left_on=None, right_on=None, on=None, suffix: str = '_right')

      Perform an full join

      :param df: Lazy DataFrame to join with.
      :type df: Tibble
      :param left_on: Join column(s) of the left DataFrame.
      :type left_on: str, list
      :param right_on: Join column(s) of the right DataFrame.
      :type right_on: str, list
      :param on: Join column(s) of both DataFrames. If set, `left_on` and `right_on` should be None.
      :type on: str, list
      :param suffix: Suffix to append to columns with a duplicate name.
      :type suffix: str

      .. rubric:: Examples

      df1.full_join(df2)
      df1.full_join(df2, on = 'x')
      df1.full_join(df2, left_on = 'left_x', right_on = 'x')


   .. py:method:: pivot_longer(self, cols=everything(), names_to='name', values_to='value')

      Pivot data from wide to long

      :param cols: List of the columns to pivot. Defaults to all columns.
      :type cols: Expr
      :param names_to: Name of the new "names" column.
      :type names_to: str
      :param values_to: Name of the new "values" column
      :type values_to: str

      .. rubric:: Examples

      >>> df = tp.Tibble({'id': ['id1', 'id2'], 'a': [1, 2], 'b': [1, 2]})
      >>> df.pivot_longer(cols = ['a', 'b'])
      >>> df.pivot_longer(cols = ['a', 'b'], names_to = 'stuff', values_to = 'things')


   .. py:method:: pivot_wider(self, names_from='name', values_from='value', id_cols=None, values_fn='first', values_fill=None)

      Pivot data from long to wide

      :param names_from: Column to get the new column names from.
      :type names_from: str
      :param values_from: Column to get the new column values from
      :type values_from: str
      :param id_cols: A set of columns that uniquely identifies each observation.
                      Defaults to all columns in the data table except for the columns specified in
                      `names_from` and `values_from`.
      :type id_cols: str, list
      :param values_fn: Function for how multiple entries per group should be dealt with.
      :type values_fn: str
      :param values_fill: If values are missing/null, what value should be filled in.
                          Can use: "backward", "forward", "mean", "min", "max", "zero", "one" or an expression
      :type values_fill: str

      .. rubric:: Examples

      >>> df = tp.Tibble({'id': [1, 1], 'variable': ['a', 'b'], 'value': [1, 2]})
      >>> df.pivot_wider(names_from = 'variable', values_from = 'value')


   .. py:method:: pull(self, var=None)

      Extract a column as a series

      :param var: Name of the column to extract. Defaults to the last column.
      :type var: str

      .. rubric:: Examples

      >>> df = tp.Tibble({'a': range(3), 'b': range(3))
      >>> df.pull('a')


   .. py:method:: relocate(self, *args, before=None, after=None)

      Move a column or columns to a new position

      :param \*args: Columns to move
      :type \*args: str, Expr

      .. rubric:: Examples

      >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
      >>> df.relocate('a', before = 'c')
      >>> df.relocate('b', after = 'c')


   .. py:method:: rename(self, *args, **kwargs)

      Rename columns

      :param \*args: Dictionary mapping of new names
      :type \*args: dict
      :param \*\*kwargs: key-value pair of new name from old name
      :type \*\*kwargs: str

      .. rubric:: Examples

      >>> df = tp.Tibble({'x': range(3), 't': range(3), 'z': ['a', 'a', 'b']})
      >>> df.rename(new_x = 'x') # dplyr interface
      >>> df.rename({'x': 'new_x'}) # pandas interface


   .. py:method:: replace_null(self, replace=None)

      Replace null values

      :param replace: Dictionary of column/replacement pairs
      :type replace: dict

      .. rubric:: Examples

      >>> df = tp.Tibble(x = [0, None], y = [None, None])
      >>> df.replace_null(dict(x = 1, y = 2))


   .. py:method:: set_names(self, nm=None)

      Change the column names of the data frame

      :param nm: A list of new names for the data frame
      :type nm: list

      .. rubric:: Examples

      >>> df = tp.Tibble(x = range(3), y = range(3))
      >>> df.set_names(['a', 'b'])


   .. py:method:: select(self, *args)

      Select or drop columns

      :param \*args: Columns to select
      :type \*args: str, Expr

      .. rubric:: Examples

      >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
      >>> df.select('a', 'b')
      >>> df.select(col('a'), col('b'))


   .. py:method:: slice(self, *args, by=None)

      Grab rows from a data frame

      :param \*args: Rows to grab
      :type \*args: int, list
      :param by: Columns to group by
      :type by: str, list

      .. rubric:: Examples

      >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
      >>> df.slice(0, 1)
      >>> df.slice(0, by = 'c')


   .. py:method:: slice_head(self, n=5, *, by=None)

      Grab top rows from a data frame

      :param n: Number of rows to grab
      :type n: int
      :param by: Columns to group by
      :type by: str, list

      .. rubric:: Examples

      >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
      >>> df.slice_head(2)
      >>> df.slice_head(1, by = 'c')


   .. py:method:: slice_tail(self, n=5, *, by=None)

      Grab bottom rows from a data frame

      :param n: Number of rows to grab
      :type n: int
      :param by: Columns to group by
      :type by: str, list

      .. rubric:: Examples

      >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
      >>> df.slice_tail(2)
      >>> df.slice_tail(1, by = 'c')


   .. py:method:: summarise(self, *args, by=None, **kwargs)

      Alias for .summarize()


   .. py:method:: summarize(self, *args, by=None, **kwargs)

      Aggregate data with summary statistics

      :param \*args: Column expressions to add or modify
      :type \*args: Expr
      :param by: Columns to group by
      :type by: str, list
      :param \*\*kwargs: Column expressions to add or modify
      :type \*\*kwargs: Expr

      .. rubric:: Examples

      >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
      >>> df.summarize(avg_a = tp.mean(col('a')))
      >>> df.summarize(avg_a = tp.mean(col('a')),
      ...              by = 'c')
      >>> df.summarize(avg_a = tp.mean(col('a')),
      ...              max_b = tp.max(col('b')))


   .. py:method:: tail(self, n=5, *, by=None)

      Alias for `.slice_tail()`


   .. py:method:: to_pandas(self)

      Convert to a polars DataFrame

      .. rubric:: Examples

      >>> df.to_pandas()


   .. py:method:: to_polars(self, shallow_copy=True)

      Convert to a polars DataFrame

      :param by_ref: Whether a shallow copy should be made
      :type by_ref: bool

      .. rubric:: Examples

      >>> df.to_polars()


   .. py:method:: write_csv(self, file=None, has_headers=True, sep=',')

      Write a data frame to a csv


   .. py:method:: write_parquet(self, file=str, compression='snappy', use_pyarrow=False, **kwargs)

      Write a data frame to a parquet



.. py:function:: desc(x)

   Mark a column to order in descending


.. py:function:: from_polars(df)

   Convert from polars DataFrame to Tibble

   :param df: pl.DataFrame to convert to a Tibble
   :type df: DataFrame

   .. rubric:: Examples

   >>> tp.from_polars(df)


.. py:function:: from_pandas(df)

   Convert from pandas DataFrame to Tibble

   :param df: pd.DataFrame to convert to a Tibble
   :type df: DataFrame

   .. rubric:: Examples

   >>> tp.from_pandas(df)


