from fastapi import APIRouter, Request
from typing import Optional
from app.models import OpeningHoursRequest, HourInfo, DAYS_ORDER, HourType
from app.utls import humanize_opening_hours

second_solution_router = APIRouter(
    prefix="/api/opening-hours",
    tags=["opening_hours"],
    responses={404: {"message": "Reply not found"}}
)

@second_solution_router.post("/second-solution")
async def huminze_opening_hours(payload: OpeningHoursRequest) -> str:
    """
    this solution is basic by looping over the hours and match the open with close

    """
    data = dict(sorted(payload.__root__.items(), key=lambda x: DAYS_ORDER[x[0]]))

    open: Optional[HourInfo] = None
    open_day: str = ''
    closed_before_open: Optional[HourInfo] = None

    week_info_dict = {}
    for day_name, hours_info in data.items():

        week_info_dict[day_name] = []
        hours_info: list[HourInfo] = sorted(hours_info, key=lambda h: h.value)

        for hour_info in hours_info:

            if hour_info.type == HourType.OPEN and not open:
                open = hour_info
                open_day = day_name
            elif hour_info.type == HourType.CLOSE and open:
                week_info_dict[open_day].append((open.value, hour_info.value))
                open = None
            elif hour_info.type == HourType.CLOSE and not open:
                closed_before_open = hour_info

    if closed_before_open and open:
        week_info_dict[open_day].append((open.value, closed_before_open.value))

    return humanize_opening_hours(week_info_dict)
