from fastapi import APIRouter, Path, Depends, HTTPException
from app.models import ServiceResponseModel, TextSentiment
from textblob import TextBlob
import re

router = APIRouter(
    include_in_schema=True,
)

@router.get("/health")
def healthz():
    return {"status": "Healthy!!!"}

@router.get("/services", response_model=list[ServiceResponseModel])
def list_services():
    return [{"message": "All Good"}]

def validate_text(text):
    if len(re.findall(r'[^A-Za-z\s]', text)) != 0:
        raise HTTPException(status_code=422, detail='Please provide only text alphabets')
    return text

@router.get("/sentiment/{text}", response_model=TextSentiment)
def get_sentiment(text: str = Path(description="Input text for sentiment analysis")):
    text = validate_text(text)
    text_blob = TextBlob(text)
    polarity, subjectivity = text_blob.sentiment

    if polarity > 0:
        type = 'positive'
    elif polarity < 0:
        type = 'negative'
    else:
        type = 'neutral'

    return TextSentiment(text=text,
                         sentiment_type=type,
                         sentiment_score=polarity)