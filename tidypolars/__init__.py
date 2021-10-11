# read version from installed package
from importlib.metadata import version
__version__ = version("tidypolars")

from .tidypolars import *
from .expr_funs import *
from .reexports import *

__all__ = tidypolars.__all__ + reexports.__all__