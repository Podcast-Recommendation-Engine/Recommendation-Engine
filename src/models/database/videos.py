from src.config.database.database_config import db_client

class VideoModel:
    COLLECTION_NAME = "videos"

    @staticmethod
    def create_collection():
        db_client.recreate_collection(
            collection_name=VideoModel.COLLECTION_NAME,
            vectors_config={
                "size": 768,
                "distance": "Cosine"
            }
        )

    @staticmethod
    def insert_video(video_id: str, embedding: list, metadata: dict):
        db_client.upsert(
            collection_name=VideoModel.COLLECTION_NAME,
            points=[
                {
                    "id": video_id,
                    "vector": embedding,
                    "payload": metadata
                }
            ]
        )