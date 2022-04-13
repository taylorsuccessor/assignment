import pandas as pd
import numpy as np
from typing import List
from pydantic import BaseModel, validator
from .datetime import Days, HourType, HourInfo, DAYS_ORDER
from fastapi import HTTPException

class OpeningHoursRequest(BaseModel):

    __root__: dict[Days, List[HourInfo]]

    @validator('__root__', pre=True, always=True)
    def validate_root_json(cls, value):

        if type(value) is not dict or len(value) == 0:
            raise ValueError("only json allowed")

        return value

def request_to_dataframe(openingHoursRequest: OpeningHoursRequest):
    """
    this function take the json data
    dict[Days, List[HourInfo]]
    and convert it to Dataframe

    | day_name  | day  | value | type |
    |-----------|------|-------|------|
    |  sunday   |   7  |  4000 | open |
    |  sunday   |   7  |  8000 | close|
    |           |      |       |      |

    then it sort it asc by day, value
    then move the first row if it's close to end
    :param: OpeningHoursRequest: dict[Days, List[HourInfo]]
    :return: DataFrame: sorted
    """
    new_data = []
    for day_name, hour_info_list in openingHoursRequest.__root__.items():
        for hour in hour_info_list:
            new_data.append({
                'day_name': day_name.name,
                'day': DAYS_ORDER[day_name],
                'type': hour.type,
                'value': hour.value
            })

    df = pd.DataFrame(new_data).sort_values(['day', 'value'])

    if len(df) % 2 == 1:
        raise HTTPException(status_code = 422, detail =  "for each open should be one close")

    if df.iloc[0].type == HourType.CLOSE:
        df = df.reindex(np.roll(df.index, shift=1))

    return df
