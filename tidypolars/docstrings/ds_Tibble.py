from tidypolars import Tibble

Tibble.arrange.__doc__ = """
    Arrange/sort rows

    Parameters
    ----------
    *args : 
        Columns to sort by
    desc : 
        Should columns be ordered in descending order

    Examples
    --------
    df = tp.Tibble({'x': ['a', 'a', 'b'], 'y': range(3)})

    # Arrange in ascending order
    df.arrange('x', 'y')

    # Arrange some columns descending
    df.arrange('x', 'y', desc = [True, False])
    """

Tibble.bind_cols.__doc__ = """
    Bind data frames by columns

    Parameters
    ----------
    df : Tibble
        Data frame to bind

    Examples
    --------
    df1 = tp.Tibble({'x': ['a', 'a', 'b'], 'y': range(3)})
    df2 = tp.Tibble({'a': ['c', 'c', 'c'], 'b': range(4, 7)})

    df1.bind_cols(df2)
    """

Tibble.bind_rows.__doc__ = """
    Bind data frames by row

    Parameters
    ----------
    df : Tibble
        Data frame to bind

    Examples
    --------
    df1 = tp.Tibble({'x': ['a', 'a', 'b'], 'y': range(3)})
    df2 = tp.Tibble({'x': ['c', 'c', 'c'], 'y': range(4, 7)})

    df1.bind_rows(df2)
    """

Tibble.distinct.__doc__ = """
    Select distinct/unique rows

    Parameters
    ----------
    *args : Union[str, Expr]
        Columns to find distinct/unique rows

    Examples
    --------
    df = tp.tibble({'a': range(3), 'b': ['a', 'a', 'b']})
    
    df.distinct()
    df.distinct('b')
    """

Tibble.filter.__doc__ = """
    Filter rows on one or more conditions

    Parameters
    ----------
    *args : Expr
        Conditions to filter by

    groupby : Union[str, Expr, List[str], List[Expr]]
        Columns to group by

    Examples
    --------
    df = tp.Tibble({'a': range(3), 'b': ['a', 'a', 'b']})
    
    df.filter(col('a') < 2, col('c') == 'a')
    df.filter((col('a') < 2) & (col('c') == 'a'))
    df.filter(col('a') <= col('a').mean(),
                groupby = 'b')
    """

Tibble.head.__doc__ = """Alias for .slice_head()"""

Tibble.mutate.__doc__ = """
    Add or modify columns

    Parameters
    ----------
    *args : Expr
        Column expressions to add or modify

    groupby : Union[str, Expr, List[str], List[Expr]]
        Columns to group by
    
    **kwargs : Expr
        Column expressions to add or modify

    Examples
    --------
    df = tp.Tibble({'a': range(3), 'b': range(3)})

    df.mutate(double_a = col('a') * 2,
                a_plus_b = col('a') + col('b'))
    
    df.mutate((col(['a', 'b]) * 2).prefix('double_'),
                a_plus_b = col('a') + col('b'))
    """

Tibble.pull.__doc__ = """
    Extract a column as a series

    Parameters
    ----------
    var : str
        Name of the column to extract. Defaults to the last column.

    Examples
    --------
    df = tp.Tibble({'a': range(3), 'b': range(3))
    
    df.pull('a')
    """

Tibble.relocate.__doc__ = """
    Move a column or columns to a new position

    Parameters
    ----------
    *args : Union[str, Expr]
        Columns to move

    Examples
    --------
    df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
    
    df.relocate('a', before = 'c')

    df.relocate('b', after = 'c')
    """

Tibble.rename.__doc__ = """
    Rename columns

    Parameters
    ----------
    *args : Dict[str, str]
        Dictionary mapping of new names

    Examples
    --------
    df = tp.Tibble({'x': range(3), 't': range(3), 'z': ['a', 'a', 'b']})
    
    df.rename({'x': 'new_x'})
    """

Tibble.select.__doc__ = """
    Select or drop columns

    Parameters
    ----------
    *args : Union[str, Expr]
        Columns to select

    Examples
    --------
    df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
    
    df.select('a', 'b')

    df.select(col('a'), col('b'))
    """

Tibble.slice.__doc__ = """
    Grab rows from a data frame

    Parameters
    ----------
    *args : Union[int, List[int]]
        Rows to grab
    
    groupby : Union[str, Expr, List[str], List[Expr]]
        Columns to group by

    Examples
    --------
    df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
    
    df.slice(0, 1)

    df.slice(0, groupby = 'c')
    """

Tibble.slice_head.__doc__ = """
    Grab top rows from a data frame

    Parameters
    ----------
    n : int
        Number of rows to grab
    
    *args :
        Currently unused
    
    groupby : Union[str, Expr, List[str], List[Expr]]
        Columns to group by

    Examples
    --------
    df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
    
    df.slice_head(2)

    df.slice_head(1, groupby = 'c')
    """

Tibble.slice_tail.__doc__ = """
    Grab bottom rows from a data frame

    Parameters
    ----------
    n : int
        Number of rows to grab
    
    *args :
        Currently unused
    
    groupby : Union[str, Expr, List[str], List[Expr]]
        Columns to group by

    Examples
    --------
    df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
    
    df.slice_tail(2)

    df.slice_tail(1, groupby = 'c')
    """

Tibble.summarize.__doc__ = """
    Aggregate data with summary statistics

    Parameters
    ----------
    *args : Expr

    groupby : Union[str, Expr, List[str], List[Expr]]
        Columns to group by

    **kwargs : Expr
        Column expressions to add or modify

    Examples
    --------
    df = tp.Tibble({'a': range(3), 'b': range(3), 'c': ['a', 'a', 'b']})
    
    df.summarize(avg_a = col('a').mean())

    df.summarize(avg_a = col('a').mean(),
                    groupby = 'c')

    df.summarize(avg_a = col('a').mean(),
                    max_b = col('b').max()))
    """

Tibble.tail.__doc__ = """Alias for .slice_tail()"""