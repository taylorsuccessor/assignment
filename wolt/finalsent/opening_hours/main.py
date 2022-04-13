from fastapi import FastAPI

from app.routers import opening_hours_router, second_solution_router

app = FastAPI()

app.include_router(opening_hours_router)
app.include_router(second_solution_router)

@app.get("/beat")
def root():
    return {"message": """
            We Checked the connections to database and other
            part of the system and we make sure it's return correct status
            """}
