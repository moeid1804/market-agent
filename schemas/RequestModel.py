from pydantic import BaseModel, Field


class MarketingRequest(BaseModel):
    query: str = Field(
        min_length=5,
        max_length=1000,
    )