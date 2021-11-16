:py:mod:`tidypolars`
====================

.. py:module:: tidypolars


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   funs/index.rst
   lubridate/index.rst
   reexports/index.rst
   stringr/index.rst
   tidypolars/index.rst
   tidyselect/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   tidypolars.Tibble



Functions
~~~~~~~~~

.. autoapisummary::

   tidypolars.abs
   tidypolars.case_when
   tidypolars.if_else
   tidypolars.lag
   tidypolars.lead
   tidypolars.read_csv
   tidypolars.read_parquet
   tidypolars.replace_null
   tidypolars.round
   tidypolars.first
   tidypolars.last
   tidypolars.max
   tidypolars.mean
   tidypolars.median
   tidypolars.min
   tidypolars.n_distinct
   tidypolars.sd
   tidypolars.sum
   tidypolars.between
   tidypolars.is_finite
   tidypolars.is_in
   tidypolars.is_infinite
   tidypolars.is_nan
   tidypolars.is_not
   tidypolars.is_not_in
   tidypolars.is_not_null
   tidypolars.is_null
   tidypolars.as_float
   tidypolars.as_integer
   tidypolars.as_string
   tidypolars.cast
   tidypolars.as_date
   tidypolars.as_datetime
   tidypolars.hour
   tidypolars.mday
   tidypolars.minute
   tidypolars.month
   tidypolars.quarter
   tidypolars.dt_round
   tidypolars.second
   tidypolars.wday
   tidypolars.week
   tidypolars.yday
   tidypolars.year
   tidypolars.paste
   tidypolars.paste0
   tidypolars.str_detect
   tidypolars.str_extract
   tidypolars.str_length
   tidypolars.str_remove_all
   tidypolars.str_remove
   tidypolars.str_replace_all
   tidypolars.str_replace
   tidypolars.str_sub
   tidypolars.str_to_lower
   tidypolars.str_to_upper
   tidypolars.str_trim
   tidypolars.desc
   tidypolars.from_pandas
   tidypolars.from_polars
   tidypolars.contains
   tidypolars.ends_with
   tidypolars.everything
   tidypolars.starts_with



Attributes
~~~~~~~~~~

.. autoapisummary::

   tidypolars.__version__
   tidypolars.col
   tidypolars.exclude
   tidypolars.lit
   tidypolars.Expr
   tidypolars.Series
   tidypolars.Int8
   tidypolars.Int16
   tidypolars.Int32
   tidypolars.Int64
   tidypolars.UInt8
   tidypolars.UInt16
   tidypolars.UInt32
   tidypolars.UInt64
   tidypolars.Float32
   tidypolars.Float64
   tidypolars.Boolean
   tidypolars.Utf8
   tidypolars.List
   tidypolars.Date
   tidypolars.Datetime
   tidypolars.Object
   tidypolars.__all__


.. py:data:: __version__
   

   

.. py:function:: abs(x)

   Absolute value

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.mutate(abs_x = tp.abs('x'))
   >>> df.mutate(abs_x = tp.abs(col('x')))


.. py:function:: case_when(expr)

   Case when

   :param expr: A logical expression
   :type expr: Expr

   .. rubric:: Examples

   >>> df = tp.Tibble(x = range(1, 4))
   >>> df.mutate(
   >>>    case_x = tp.case_when(col('x') < 2).then(1)
   >>>             .when(col('x') < 3).then(2)
   >>>             .otherwise(0)
   >>> )


.. py:function:: if_else(condition, true, false)

   If Else

   :param condition: A logical expression
   :type condition: Expr
   :param true: Value if the condition is true
   :param false: Value if the condition is false

   .. rubric:: Examples

   >>> df = tp.Tibble(x = range(1, 4))
   >>> df.mutate(if_x = tp.if_else(col('x') < 2, 1, 2))


.. py:function:: lag(x, n: int = 1, default=None)

   Get lagging values

   :param x: Column to operate on
   :type x: Expr, Series
   :param n: Number of positions to lag by
   :type n: int
   :param default: Value to fill in missing values
   :type default: optional

   .. rubric:: Examples

   >>> df.mutate(lag_x = tp.lag(col('x')))
   >>> df.mutate(lag_x = tp.lag('x'))


.. py:function:: lead(x, n: int = 1, default=None)

   Get leading values

   :param x: Column to operate on
   :type x: Expr, Series
   :param n: Number of positions to lead by
   :type n: int
   :param default: Value to fill in missing values
   :type default: optional

   .. rubric:: Examples

   >>> df.mutate(lead_x = tp.lead(col('x')))
   >>> df.mutate(lead_x = col('x').lead())


.. py:function:: read_csv(file: str, *args, **kwargs)

   Simple wrapper around polars.read_csv


.. py:function:: read_parquet(source: str, *args, **kwargs)

   Simple wrapper around polars.read_parquet


.. py:function:: replace_null(x, replace=None)

   Replace null values

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df = tp.Tibble(x = [0, None], y = [None, None])
   >>> df.mutate(x = tp.replace_null(col('x'), 1))


.. py:function:: round(x, decimals=0)

   Get column standard deviation

   :param x: Column to operate on
   :type x: Expr, Series
   :param decimals: Decimals to round to
   :type decimals: int

   .. rubric:: Examples

   >>> df.mutate(x = tp.round(col('x')))


.. py:function:: first(x)

   Get first value

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.summarize(first_x = tp.first('x'))
   >>> df.summarize(first_x = tp.first(col('x')))


.. py:function:: last(x)

   Get last value

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.summarize(last_x = tp.last('x'))
   >>> df.summarize(last_x = tp.last(col('x')))


.. py:function:: max(x)

   Get column max

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.summarize(max_x = tp.max('x'))
   >>> df.summarize(max_x = tp.max(col('x')))


.. py:function:: mean(x)

   Get column mean

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.summarize(mean_x = tp.mean('x'))
   >>> df.summarize(mean_x = tp.mean(col('x')))


.. py:function:: median(x)

   Get column median

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.summarize(median_x = tp.median('x'))
   >>> df.summarize(median_x = tp.median(col('x')))


.. py:function:: min(x)

   Get column minimum

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.summarize(min_x = tp.min('x'))
   >>> df.summarize(min_x = tp.min(col('x')))


.. py:function:: n_distinct(x)

   Get number of distinct values in a column

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.summarize(min_x = tp.n_distinct('x'))
   >>> df.summarize(min_x = tp.n_distinct(col('x')))


.. py:function:: sd(x)

   Get column standard deviation

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.summarize(sd_x = tp.sd('x'))
   >>> df.summarize(sd_x = tp.sd(col('x')))


.. py:function:: sum(x)

   Get column sum

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.summarize(sum_x = tp.sum('x'))
   >>> df.summarize(sum_x = tp.sum(col('x')))


.. py:function:: between(x, left, right)

   Test if values of a column are between two values

   :param x: Column to operate on
   :type x: Expr, Series
   :param left: Value to test if column is greater than or equal to
   :type left: int
   :param right: Value to test if column is less than or equal to
   :type right: int

   .. rubric:: Examples

   >>> df = tp.Tibble(x = range(4))
   >>> df.filter(tp.between(col('x'), 1, 3))


.. py:function:: is_finite(x)

   Test if values of a column are finite

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df = tp.Tibble(x = [1.0, float('inf')])
   >>> df.filter(tp.is_finite(col('x')))


.. py:function:: is_in(x, y)

   Test if values of a column are in a list of values

   :param x: Column to operate on
   :type x: Expr, Series
   :param y: List to test against
   :type y: list

   .. rubric:: Examples

   >>> df = tp.Tibble(x = range(3))
   >>> df.filter(tp.is_in(col('x'), [1, 2]))


.. py:function:: is_infinite(x)

   Test if values of a column are infinite

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df = tp.Tibble(x = [1.0, float('inf')])
   >>> df.filter(tp.is_infinite(col('x')))


.. py:function:: is_nan(x)

   Test if values of a column are nan

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df = tp.Tibble(x = range(3))
   >>> df.filter(tp.is_nan(col('x')))


.. py:function:: is_not(x)

   Flip values of a boolean series

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df = tp.Tibble(x = range(3))
   >>> df.filter(tp.is_not(col('x') < 2))


.. py:function:: is_not_in(x, y)

   Test if values of a column are not in a list of values

   :param x: Column to operate on
   :type x: Expr, Series
   :param y: List to test against
   :type y: list

   .. rubric:: Examples

   >>> df = tp.Tibble(x = range(3))
   >>> df.filter(tp.is_not_in(col('x'), [1, 2]))


.. py:function:: is_not_null(x)

   Test if values of a column are not null

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df = tp.Tibble(x = range(3))
   >>> df.filter(tp.is_not_in(col('x'), [1, 2]))


.. py:function:: is_null(x)

   Test if values of a column are null

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df = tp.Tibble(x = range(3))
   >>> df.filter(tp.is_not_in(col('x'), [1, 2]))


.. py:function:: as_float(x, dtype=pl.Float64)

   Convert to integer. Defaults to Float64.

   :param x: Column to operate on
   :type x: Expr, Series
   :param dtype: Type to convert to
   :type dtype: DataType

   .. rubric:: Examples

   >>> df.mutate(abs_x = tp.as_float(col('x')))


.. py:function:: as_integer(x, dtype=pl.Int64)

   Convert to integer. Defaults to Int64.

   :param x: Column to operate on
   :type x: Expr, Series
   :param dtype: Type to convert to
   :type dtype: DataType

   .. rubric:: Examples

   >>> df.mutate(abs_x = tp.as_integer(col('x')))


.. py:function:: as_string(x, dtype=pl.Utf8)

   Convert to string. Defaults to Utf8.

   :param x: Column to operate on
   :type x: Expr, Series
   :param dtype: Type to convert to
   :type dtype: DataType

   .. rubric:: Examples

   >>> df.mutate(abs_x = tp.as_string(col('x')))


.. py:function:: cast(x, dtype)

   General type conversion.

   :param x: Column to operate on
   :type x: Expr, Series
   :param dtype: Type to convert to
   :type dtype: DataType

   .. rubric:: Examples

   >>> df.mutate(abs_x = tp.cast(col('x'), tp.Float64))


.. py:function:: as_date(x, fmt=None)

   Convert a string to a Date

   :param x: Column to operate on
   :type x: Expr, Series
   :param fmt: "yyyy-mm-dd"
   :type fmt: str

   .. rubric:: Examples

   >>> df = tp.Tibble(x = ['2021-01-01', '2021-10-01'])
   >>> df.mutate(date_x = tp.as_date(col('x')))


.. py:function:: as_datetime(x, fmt=None)

   Convert a string to a Datetime

   :param x: Column to operate on
   :type x: Expr, Series
   :param fmt: "yyyy-mm-dd"
   :type fmt: str

   .. rubric:: Examples

   >>> df = tp.Tibble(x = ['2021-01-01', '2021-10-01'])
   >>> df.mutate(date_x = tp.as_datetime(col('x')))


.. py:function:: hour(x)

   Extract the hour from a datetime

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.mutate(hour = tp.as_hour(col('x')))


.. py:function:: mday(x)

   Extract the month day from a date from 1 to 31.

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.mutate(monthday = tp.mday(col('x')))


.. py:function:: minute(x)

   Extract the minute from a datetime

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.mutate(hour = tp.minute(col('x')))


.. py:function:: month(x)

   Extract the month from a date

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.mutate(year = tp.month(col('x')))


.. py:function:: quarter(x)

   Extract the quarter from a date

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.mutate(quarter = tp.quarter(col('x')))


.. py:function:: dt_round(x, rule, n)

   Round the datetime

   :param x: Column to operate on
   :type x: Expr, Series
   :param rule: Units of the downscaling operation.
                Any of:
                    - "month"
                    - "week"
                    - "day"
                    - "hour"
                    - "minute"
                    - "second"
   :type rule: str
   :param n: Number of units (e.g. 5 "day", 15 "minute".
   :type n: int

   .. rubric:: Examples

   >>> df.mutate(monthday = tp.mday(col('x')))


.. py:function:: second(x)

   Extract the second from a datetime

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.mutate(hour = tp.minute(col('x')))


.. py:function:: wday(x)

   Extract the weekday from a date from sunday = 1 to saturday = 7.

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.mutate(weekday = tp.wday(col('x')))


.. py:function:: week(x)

   Extract the week from a date

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.mutate(week = tp.week(col('x')))


.. py:function:: yday(x)

   Extract the year day from a date from 1 to 366.

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.mutate(yearday = tp.yday(col('x')))


.. py:function:: year(x)

   Extract the year from a date

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.mutate(year = tp.year(col('x')))


.. py:data:: col
   

   

.. py:data:: exclude
   

   

.. py:data:: lit
   

   

.. py:data:: Expr
   

   

.. py:data:: Series
   

   

.. py:data:: Int8
   

   

.. py:data:: Int16
   

   

.. py:data:: Int32
   

   

.. py:data:: Int64
   

   

.. py:data:: UInt8
   

   

.. py:data:: UInt16
   

   

.. py:data:: UInt32
   

   

.. py:data:: UInt64
   

   

.. py:data:: Float32
   

   

.. py:data:: Float64
   

   

.. py:data:: Boolean
   

   

.. py:data:: Utf8
   

   

.. py:data:: List
   

   

.. py:data:: Date
   

   

.. py:data:: Datetime
   

   

.. py:data:: Object
   

   

.. py:function:: paste(*args, sep=' ')

   Concatenate strings together

   :param args: Columns and or strings to concatenate
   :type args: Expr, str

   .. rubric:: Examples

   >>> df = tp.Tibble(x = ['a', 'b', 'c'])
   >>> df.mutate(x_end = tp.paste(col('x'), 'end', sep = '_'))


.. py:function:: paste0(*args)

   Concatenate strings together with no separator

   :param args: Columns and or strings to concatenate
   :type args: Expr, str

   .. rubric:: Examples

   >>> df = tp.Tibble(x = ['a', 'b', 'c'])
   >>> df.mutate(xend = tp.paste0(col('x'), 'end'))


.. py:function:: str_detect(string, pattern, negate=False)

   Detect the presence or absence of a pattern in a string

   :param string: Input series to operate on
   :type string: str
   :param pattern: Pattern to look for
   :type pattern: str
   :param negate: If True, return non-matching elements
   :type negate: bool

   .. rubric:: Examples

   >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
   >>> df.mutate(x = str_detect('name', 'a'))
   >>> df.mutate(x = str_detect('name', ['a', 'e']))


.. py:function:: str_extract(string, pattern)

   Extract the target capture group from provided patterns

   :param string: Input series to operate on
   :type string: str
   :param pattern: Pattern to look for
   :type pattern: str

   .. rubric:: Examples

   >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
   >>> df.mutate(x = str_extract(col('name'), 'e'))


.. py:function:: str_length(string)

   Length of a string

   :param string: Input series to operate on
   :type string: str

   .. rubric:: Examples

   >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
   >>> df.mutate(x = str_length(col('name')))


.. py:function:: str_remove_all(string, pattern)

   Removes all matched patterns in a string

   :param string: Input series to operate on
   :type string: str
   :param pattern: Pattern to look for
   :type pattern: str

   .. rubric:: Examples

   >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
   >>> df.mutate(x = str_remove_all(col('name'), 'a'))


.. py:function:: str_remove(string, pattern)

   Removes the first matched patterns in a string

   :param string: Input series to operate on
   :type string: str
   :param pattern: Pattern to look for
   :type pattern: str

   .. rubric:: Examples

   >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
   >>> df.mutate(x = str_remove(col('name'), 'a'))


.. py:function:: str_replace_all(string, pattern, replacement)

   Replaces all matched patterns in a string

   :param string: Input series to operate on
   :type string: str
   :param pattern: Pattern to look for
   :type pattern: str
   :param replacement: String that replaces anything that matches the pattern
   :type replacement: str

   .. rubric:: Examples

   >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
   >>> df.mutate(x = str_replace_all(col('name'), 'a', 'A'))


.. py:function:: str_replace(string, pattern, replacement)

   Replaces the first matched patterns in a string

   :param string: Input series to operate on
   :type string: str
   :param pattern: Pattern to look for
   :type pattern: str
   :param replacement: String that replaces anything that matches the pattern
   :type replacement: str

   .. rubric:: Examples

   >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
   >>> df.mutate(x = str_replace(col('name'), 'a', 'A'))


.. py:function:: str_sub(string, start=0, end=None)

   Extract portion of string based on start and end inputs

   :param string: Input series to operate on
   :type string: str
   :param start: First position of the character to return
   :type start: int
   :param end: Last position of the character to return
   :type end: int

   .. rubric:: Examples

   >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
   >>> df.mutate(x = str_sub(col('name'), 0, 3))


.. py:function:: str_to_lower(string)

   Convert case of a string

   :param string: Convert case of this string
   :type string: str

   .. rubric:: Examples

   >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
   >>> df.mutate(x = str_to_lower(col('name')))


.. py:function:: str_to_upper(string)

   Convert case of a string

   :param string: Convert case of this string
   :type string: str

   .. rubric:: Examples

   >>> df = tp.Tibble(name = ['apple', 'banana', 'pear', 'grape'])
   >>> df.mutate(x = str_to_upper(col('name')))


.. py:function:: str_trim(string, side='both')

   Trim whitespace

   :param string: Column or series to operate on
   :type string: Expr, Series
   :param side:
                One of:
                    * "both"
                    * "left"
                    * "right"
   :type side: str

   .. rubric:: Examples

   >>> df = tp.Tibble(x = [' a ', ' b ', ' c '])
   >>> df.mutate(x = tp.str_trim(col('x')))


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


.. py:function:: from_pandas(df)

   Convert from pandas DataFrame to Tibble

   :param df: pd.DataFrame to convert to a Tibble
   :type df: DataFrame

   .. rubric:: Examples

   >>> tp.from_pandas(df)


.. py:function:: from_polars(df)

   Convert from polars DataFrame to Tibble

   :param df: pl.DataFrame to convert to a Tibble
   :type df: DataFrame

   .. rubric:: Examples

   >>> tp.from_polars(df)


.. py:function:: contains(match, ignore_case=True)

   Contains a literal string

   :param match: String to match columns
   :type match: str
   :param ignore_case: If TRUE, the default, ignores case when matching names.
   :type ignore_case: bool

   .. rubric:: Examples

   >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
   >>> df.select(contains('c'))


.. py:function:: ends_with(match, ignore_case=True)

   Ends with a suffix

   :param match: String to match columns
   :type match: str
   :param ignore_case: If TRUE, the default, ignores case when matching names.
   :type ignore_case: bool

   .. rubric:: Examples

   >>> df = tp.Tibble({'a': range(3), 'b_code': range(3), 'c_code': ['a', 'a', 'b']})
   >>> df.select(ends_with('code'))


.. py:function:: everything()

   Selects all columns

   .. rubric:: Examples

   >>> df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
   >>> df.select(everything())


.. py:function:: starts_with(match, ignore_case=False)

   Starts with a prefix

   :param match: String to match columns
   :type match: str
   :param ignore_case: If TRUE, the default, ignores case when matching names.
   :type ignore_case: bool

   .. rubric:: Examples

   >>> df = tp.Tibble({'a': range(3), 'add': range(3), 'sub': ['a', 'a', 'b']})
   >>> df.select(starts_with('a'))


.. py:data:: __all__
   

   

