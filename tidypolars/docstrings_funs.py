import tidypolars as tp

tp.lag.__doc__ = """
    Get lagging values

    Parameters
    ----------
    expr : Expr
        Column to operate on

    n : int
        Number of positions to lag by

    default : optional
        Value to fill in missing values

    Examples
    --------
    df.mutate(lag_x = tp.lag(col('x')))
    df.mutate(lag_x = col('x').lag())
    """

tp.lead.__doc__ = """
    Get leading values

    Parameters
    ----------
    expr : Expr
        Column to operate on

    n : int
        Number of positions to lead by

    default : optional
        Value to fill in missing values

    Examples
    --------
    df.mutate(lead_x = tp.lead(col('x')))
    df.mutate(lead_x = col('x').lead())
    """