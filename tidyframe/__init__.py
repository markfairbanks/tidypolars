# read version from installed package
from importlib.metadata import version
__version__ = version("tidyframe")

from .tidyframe import *