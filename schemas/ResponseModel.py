from pydantic import BaseModel, Field

class LLMModel(BaseModel):
    target_segments: list[str]
    campaign_strategy: str
    channels: list[str]
    content_ideas: list[str]
    kpis: list[str]

class ResponseModel(LLMModel):
    source: list[str]
    confidence: float = Field(
        ge=0.0,
        le=1.0,
    )
