:py:mod:`tidypolars.stringr`
============================

.. py:module:: tidypolars.stringr


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   tidypolars.stringr.paste
   tidypolars.stringr.paste0
   tidypolars.stringr.str_detect
   tidypolars.stringr.str_extract
   tidypolars.stringr.str_length
   tidypolars.stringr.str_sub
   tidypolars.stringr.str_remove_all
   tidypolars.stringr.str_remove
   tidypolars.stringr.str_replace_all
   tidypolars.stringr.str_replace
   tidypolars.stringr.str_to_lower
   tidypolars.stringr.str_to_upper
   tidypolars.stringr.str_trim



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


