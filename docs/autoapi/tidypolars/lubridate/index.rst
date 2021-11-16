:py:mod:`tidypolars.lubridate`
==============================

.. py:module:: tidypolars.lubridate


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   tidypolars.lubridate.as_date
   tidypolars.lubridate.as_datetime
   tidypolars.lubridate.hour
   tidypolars.lubridate.mday
   tidypolars.lubridate.minute
   tidypolars.lubridate.month
   tidypolars.lubridate.quarter
   tidypolars.lubridate.dt_round
   tidypolars.lubridate.second
   tidypolars.lubridate.wday
   tidypolars.lubridate.week
   tidypolars.lubridate.yday
   tidypolars.lubridate.year



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


