from fastapi import APIRouter, HTTPException
from app.models import OpeningHoursRequest, HourType, DAYS_ORDER, request_to_dataframe
from app.utls import humanize_opening_hours
from pandas.core.frame import DataFrame


opening_hours_router = APIRouter(
    prefix="/api/opening-hours",
    tags=["opening_hours"],
    responses={404: {"message": "Reply not found"}}
)

@opening_hours_router.post("/")
async def huminze_opening_hours(payload: OpeningHoursRequest) -> str:
    """
    this solution is to convert the data to dataframe \

    | day_name  | day  | value | type |
    |-----------|------|-------|------|
    |  sunday   |   7  |  4000 | open |
    |  sunday   |   7  |  8000 | close|
    |           |      |       |      |

    we sort data by [day, value]
    and loop by two rows so we have open -> close and open day

    - if we start with close row we move it to the end
    - if the number of rows not even the data not valid
    - if we have two open after each other directly the data not valid

    """
    df: DataFrame = request_to_dataframe(payload)

    week_info_dict: dict[str, tuple[int, int]] = {}

    for i in range(0, len(df), 2):
        open = df.iloc[i]
        close = df.iloc[i + 1]

        if open.type != HourType.OPEN or close.type != HourType.CLOSE:
            raise HTTPException(status_code = 422, detail =  "for each open should be one close")

        week_info_dict.setdefault(open.day_name,[]).append((open.value, close.value))

    # this part of the code just to add closed days and sort them

    for day_name in payload.__root__:
        if day_name.name not in week_info_dict:
            week_info_dict[day_name] = []

    week_info_dict = dict(sorted(week_info_dict.items(), key=lambda x: DAYS_ORDER[x[0].lower()]))

    return humanize_opening_hours(week_info_dict)

