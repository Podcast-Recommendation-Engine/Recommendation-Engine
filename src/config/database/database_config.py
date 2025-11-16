from qdrant_client import QdrantClient
import os
import dotenv
dotenv.load_dotenv()

db_client = QdrantClient(host=os.getenv("QDRANT_HOST", "localhost"), port=int(os.getenv("QDRANT_PORT", 6333)))
VIDEO_COLLECTION_NAME = "videos"

# Ensure the video collection exists
db_client.recreate_collection(
    collection_name=VIDEO_COLLECTION_NAME,
    vectors_config={
        "size": 768,
        "distance": "Cosine"
    }
)