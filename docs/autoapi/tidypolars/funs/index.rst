:py:mod:`tidypolars.funs`
=========================

.. py:module:: tidypolars.funs


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   tidypolars.funs.as_float
   tidypolars.funs.as_integer
   tidypolars.funs.as_string
   tidypolars.funs.abs
   tidypolars.funs.between
   tidypolars.funs.case_when
   tidypolars.funs.cast
   tidypolars.funs.first
   tidypolars.funs.if_else
   tidypolars.funs.is_finite
   tidypolars.funs.is_in
   tidypolars.funs.is_infinite
   tidypolars.funs.is_not
   tidypolars.funs.is_nan
   tidypolars.funs.is_not_in
   tidypolars.funs.is_not_null
   tidypolars.funs.is_null
   tidypolars.funs.lag
   tidypolars.funs.last
   tidypolars.funs.lead
   tidypolars.funs.max
   tidypolars.funs.mean
   tidypolars.funs.median
   tidypolars.funs.min
   tidypolars.funs.n_distinct
   tidypolars.funs.read_csv
   tidypolars.funs.read_parquet
   tidypolars.funs.replace_null
   tidypolars.funs.round
   tidypolars.funs.sd
   tidypolars.funs.sum



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


.. py:function:: abs(x)

   Absolute value

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.mutate(abs_x = tp.abs('x'))
   >>> df.mutate(abs_x = tp.abs(col('x')))


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


.. py:function:: cast(x, dtype)

   General type conversion.

   :param x: Column to operate on
   :type x: Expr, Series
   :param dtype: Type to convert to
   :type dtype: DataType

   .. rubric:: Examples

   >>> df.mutate(abs_x = tp.cast(col('x'), tp.Float64))


.. py:function:: first(x)

   Get first value

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.summarize(first_x = tp.first('x'))
   >>> df.summarize(first_x = tp.first(col('x')))


.. py:function:: if_else(condition, true, false)

   If Else

   :param condition: A logical expression
   :type condition: Expr
   :param true: Value if the condition is true
   :param false: Value if the condition is false

   .. rubric:: Examples

   >>> df = tp.Tibble(x = range(1, 4))
   >>> df.mutate(if_x = tp.if_else(col('x') < 2, 1, 2))


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


.. py:function:: is_not(x)

   Flip values of a boolean series

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df = tp.Tibble(x = range(3))
   >>> df.filter(tp.is_not(col('x') < 2))


.. py:function:: is_nan(x)

   Test if values of a column are nan

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df = tp.Tibble(x = range(3))
   >>> df.filter(tp.is_nan(col('x')))


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


.. py:function:: last(x)

   Get last value

   :param x: Column to operate on
   :type x: Expr, Series

   .. rubric:: Examples

   >>> df.summarize(last_x = tp.last('x'))
   >>> df.summarize(last_x = tp.last(col('x')))


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


