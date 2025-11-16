from fastapi import APIRouter, Depends, HTTPException
from src.services.embedding.embed import EmbeddingServiceClient
from src.models.requests.embedding import VideoMetaContentEmbeddingRequest
from src.repositories.videos.create_video import CreateVideoRepository

router = APIRouter(prefix="/embedding")
embedding_client = EmbeddingServiceClient()
create_video_repository = CreateVideoRepository()

@router.post("/videos")
def embed_text(data: VideoMetaContentEmbeddingRequest):
    try:
        embedding = embedding_client.embed_text(data.meta_content)
        create_video_repository.insert_video(video_id=data.video_id, embedding=embedding, metadata=data.meta_content)

        return {"message": "Video embedding created successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))