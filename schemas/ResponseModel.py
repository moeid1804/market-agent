from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    target_segments: list[str]
    campaign_strategy: str
    channels: list[str]
    content_ideas: list[str]
    kpis: list[str]
    confidence: float=Field(ge=0.0, le=1.0)
    sources: list[str]