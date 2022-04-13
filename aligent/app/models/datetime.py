from pydantic import BaseModel, Field
from typing import List
from enum import Enum

class Days(str, Enum):
    SUNDAY = 'sunday'
    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'


DAYS_ORDER = {
    Days.MONDAY: 1,
    Days.TUESDAY: 2,
    Days.WEDNESDAY: 3,
    Days.THURSDAY: 4,
    Days.FRIDAY: 5,
    Days.SATURDAY: 6,
    Days.SUNDAY: 7
}

class HourType(str, Enum):
    OPEN = 'open'
    CLOSE = 'close'

class HourInfo(BaseModel):
    type: HourType
    value: int = Field(..., ge=0, le=86399)
