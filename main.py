from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import (
    BaseModel,
    Field
)

from endpoints import predict

# ----------------------------------------------------------------
# host app
app = FastAPI(
    title="Demo-API: Root",
    description="Demo FastAPI project",
    version="0.0"
)


# --------------------------------------------------------------------------------
# Setup origins and cors (mostly for admin panels)

origins = [
    "http://localhost:3000",
    # add dev, qa, prod urls here.
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class DemoError(BaseModel):
    user_msg: str = Field(
        "Invalid request to server", title="An error message to display for the user", example="Invalid request to server"
    )
    msg: int = Field(
        None, title="An error message that may contain techincal jargon and be messy", example="Either an auto-generated error or a custom verbose error"
    )

DEFAULT_RESPONSE_CODES = {
    422: {},
    400: {
        "description": "Bad Request",
        'model': DemoError
    }
}


@app.get("/")
async def root() -> any:
    return {"message": "Demo Ping Pong"}


# URL Routes to our endpoints

app.include_router(
    users.router,
    prefix="/users",
    tags=["Users"],
    responses=DEFAULT_RESPONSE_CODES
)

