from fastapi import APIRouter, Depends, HTTPException
from src.services.embedding.embed import EmbeddingServiceClient
from src.models.requests.videos_recommendation import VideoRecommendationRequest
from src.repositories.videos.fetch_videos import FetchVideoRepository

router = APIRouter(prefix="/videos-recommendation")
embedding_client = EmbeddingServiceClient()
fetch_video_repository = FetchVideoRepository()

@router.post("/")
def recommend_videos(data: VideoRecommendationRequest):
    try:
        # Get embedding for the input text
        embedding = embedding_client.embed_text(data.text)

        # Fetch similar videos from the database
        videos = fetch_video_repository.fetch_video(embedding, 15)

        return {"videos": videos}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
