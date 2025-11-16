from pydantic import BaseModel


class VideoMetaContentEmbeddingRequest(BaseModel):
    meta_content: str
    video_id: str