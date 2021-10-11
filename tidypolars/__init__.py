# read version from installed package
from importlib.metadata import version
__version__ = version("tidypolars")

from .tidypolars import *
from .expr_funs import *

__all__ = tidypolars.__all__ + expr_funs.__all__