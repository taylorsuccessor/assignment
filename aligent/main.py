from fastapi import FastAPI
from datetime import datetime
from app.routers import opening_hours_router, second_solution_router

app = FastAPI()

# app.include_router(opening_hours_router)
# app.include_router(second_solution_router)

from pydantic import BaseModel, Field

from enum import Enum

class ResponseType(str, Enum):
    SECONDS = 'seconds'
    MINUTES = 'minutes'
    HOURS = 'hours'
    YEARS = 'years'



class DifferenceDatetimeRequest(BaseModel):
    from_datetime: datetime = Field(..., example="2019-04-01T00:00:00.000Z", description="ISO 8601 format")
    to_datetime: datetime = Field(..., example="2019-04-04T00:00:00.000Z", description="ISO 8601 format")
    response_type: ResponseType = Field(..., example=",".join([t.value for t in ResponseType]), description="type of response")


class DifferenceDatetimeResponse(BaseModel):
    days_number: int
    weekdays_number: int
    weeks_number: int

class DifferenceDatetime:

    def __int__(request: DifferenceDatetimeRequest):
        pass

    def get():
        pass


@app.post("/api/difference-between-dates")
def difference_between_dates(request: DifferenceDatetimeRequest):
    return (request.to_datetime - request.from_datetime) / (60 * 60)

@app.get("/beat")
def root():
    return {"message": """
            We Checked the connections to database and other
            part of the system and we make sure it's return correct status
            """}
