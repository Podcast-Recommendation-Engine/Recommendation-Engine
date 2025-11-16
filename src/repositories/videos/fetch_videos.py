from src.config.database.database_config import db_client, VIDEO_COLLECTION_NAME

class FetchVideoRepository:
    @staticmethod
    def fetch_video(embedding: list, top_k: int):
        return db_client.search(
          collection_name=VIDEO_COLLECTION_NAME,
          query_vector=embedding,
          limit=top_k
        )