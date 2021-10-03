# read version from installed package
from importlib.metadata import version
from importlib import find_loader

try:
    find_loader('tidypolars')
    __version__ = version("tidypolars")
    from .tidypolars import *
except:
    import tidypolars
    from .tidypolars import *