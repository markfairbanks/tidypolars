# read version from installed package
from importlib.metadata import version
__version__ = version("tidypolars")

from .tidypolars import (
    Tibble,
    col,
    Expr,
    Series
)
from .funs import lag, lead

# __all__ = tidypolars.__all__ + funs.__all__