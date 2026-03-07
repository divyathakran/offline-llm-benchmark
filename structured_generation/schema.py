from pydantic import BaseModel, Field


class StructuredResponse(BaseModel):
    topic: str = Field(description="Main topic of the response")
    summary: str = Field(description="Short explanation")
    confidence: float = Field(description="Confidence score between 0 and 1")