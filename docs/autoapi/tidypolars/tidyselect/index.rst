:py:mod:`tidypolars.tidyselect`
===============================

.. py:module:: tidypolars.tidyselect


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   tidypolars.tidyselect.contains
   tidypolars.tidyselect.ends_with
   tidypolars.tidyselect.everything
   tidypolars.tidyselect.starts_with



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


