# read version from installed package
try:
    from importlib.metadata import version
    __version__ = version("tidypolars")
except:
    __version__ = ""

from .funs import *
from .lubridate import *
from .reexports import *
from .stringr import *
from .tibble_df import *
from .tidyselect import *

__all__ = (
    funs.__all__ +
    lubridate.__all__ +
    reexports.__all__ +
    stringr.__all__ +
    tibble_df.__all__ +
    tidyselect.__all__ 
)