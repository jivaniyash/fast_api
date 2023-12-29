from pydantic import BaseModel


class ServiceResponseModel(BaseModel):
    message: str

class TextSentiment(BaseModel):
    text: str
    sentiment_type: str
    sentiment_score: float
    