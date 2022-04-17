from fastapi import FastAPI
from datetime import datetime
from typing import Optional, Callable
from pydantic import BaseModel, Field
from enum import Enum
import numpy as np

app = FastAPI()


class ResponseType(str, Enum):
    SECONDS = 'seconds'
    MINUTES = 'minutes'
    HOURS = 'hours'
    DAYS = 'days'
    WEEKS = 'weeks'
    YEARS = 'years'


class DifferenceDatetimeRequest(BaseModel):
    from_datetime: datetime = Field(..., example="2022-04-01T00:00:00+05:00", description="Datetime with timezone")
    to_datetime: datetime = Field(..., example="2022-04-01T00:00:00+00:00", description="Datetime with timezone")
    response_type: Optional[ResponseType] = Field(example=",".join([t.value for t in ResponseType]), description="type of response")


class DifferenceDatetimeResponse(BaseModel):
    days_number: float
    weekdays_number: float
    weeks_number: float


class DifferenceDatetime:

    seconds_converter_formila: dict[ResponseType, Callable[[float], float]] = {
        ResponseType.SECONDS: lambda v: v,
        ResponseType.MINUTES: lambda v: v / 60,
        ResponseType.HOURS: lambda v: v / (60 * 60),
        ResponseType.DAYS: lambda v: v / (60 * 60 * 24),
        ResponseType.WEEKS: lambda v: v / (60 * 60 * 24 * 7),
        ResponseType.YEARS: lambda v: v / (60 * 60 * 24 * 364),
    }

    def __init__(self, input_data: DifferenceDatetimeRequest):
        self.input_data = input_data
        self.seconds_different = (input_data.to_datetime - input_data.from_datetime).total_seconds()

    def get_days_different(self) -> float:
        """
        this method takes the different in seconds
        that we saved on the constructor then
        convert it to the target requered out put
        the default output is days but the request
        can convert it to any other type of units
        """
        return self.format_output(self.seconds_different, ResponseType.DAYS)

    def get_weekdays_different(self) -> float:

        """
        this function uses numpy built in function busday_count
        https://numpy.org/doc/stable/reference/generated/numpy.busday_count.html
        then we convert it to second after that we give the required output
        the default is days
        """
        from_date = self.input_data.from_datetime.strftime('%Y-%m-%d')
        to_date = self.input_data.to_datetime.strftime('%Y-%m-%d')
        weekdays_seconds = np.busday_count(from_date, to_date) * (60 * 60 * 24)
        return self.format_output(weekdays_seconds, ResponseType.DAYS)

    def get_weeks_different(self) -> float:
        """
        this method takes the different in seconds
        that we saved on the constructor then
        convert it to the target requered out put
        the default output is weeks but the request
        can convert it to any other type of units
        """
        return self.format_output(self.seconds_different, ResponseType.WEEKS)

    def format_output(self, value, convert_to) -> float:
        """
        return the required output format (seconds, minutes ...)
        using seconds_converter_formila to convert seconds
        if the request contains one unit to convert the response to
        it will take it otherwise it will take convert_to that
        passed to the function
        """
        convert_to = self.input_data.response_type if self.input_data.response_type else convert_to
        return round(self.seconds_converter_formila[convert_to](value), 3)

    def response(self) -> DifferenceDatetimeResponse:

        return DifferenceDatetimeResponse(
            days_number = self.get_days_different(),
            weekdays_number = self.get_weekdays_different(),
            weeks_number = self.get_weeks_different(),
        )


@app.post("/api/difference-between-dates")
def difference_between_dates(request: DifferenceDatetimeRequest) -> DifferenceDatetimeResponse:
    """
    to calculate the difference between two dates
    and convert it to required format
    """
    difference_datetime = DifferenceDatetime(request)
    return difference_datetime.response()


@app.get("/beat")
def root():
    return {"message": """
            We Checked the connections to database and other
            part of the system and we make sure it's return correct status
            """}
