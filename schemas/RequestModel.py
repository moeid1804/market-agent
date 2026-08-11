from pydantic import BaseModel, Field


class RequestModel(BaseModel):
    query: str = Field(
        min_length=5,
        max_length=1000,
    )