from src.config.database.database_config import db_client, VIDEO_COLLECTION_NAME

class CreateVideoRepository:
    @staticmethod
    def insert_video(video_id: str, embedding: list, metadata: dict):
        db_client.upsert(
            collection_name=VIDEO_COLLECTION_NAME,
            points=[
                {
                    "id": video_id,
                    "vector": embedding,
                    "payload": metadata
                }
            ]
        )