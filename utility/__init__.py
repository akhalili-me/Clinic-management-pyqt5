from .Numbers import *
from .Dates import *
from .Charts import *
from .Images import *
from .LoadingValues import *
from .Messages import *
from .Validators import *

from enum import Enum

class TimeIntervals(Enum):
    LAST_SIX_MONTHS = "شش ماه گذشته"
    LAST_THREE_MONTHS = "سه ماه گذشته"
    CURRENT_MONTH = "ماه جاری"
    LAST_YEAR = "سال گذشته"
    CURRENT_YEAR = "سال جاری"