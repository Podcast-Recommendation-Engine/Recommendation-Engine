from pydantic import BaseModel


class VideoRecommendationRequest(BaseModel):
    content: str