# read version from installed package
from importlib.metadata import version
__version__ = version("tidypolars")

from .funs import *
from .lubridate import *
from .reexports import *
from .stringr import *
from .tidypolars import *
from .tidyselect import *

__all__ = (
    funs.__all__ +
    lubridate.__all__ +
    reexports.__all__ +
    stringr.__all__ +
    tidypolars.__all__ +
    tidyselect.__all__ 
)