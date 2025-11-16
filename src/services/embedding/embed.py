import requests
import os
import dotenv
dotenv.load_dotenv()

class EmbeddingServiceClient:
    def __init__(self):
        self.base_url = os.getenv("EMBEDDING_SERVICE_URL", "")
        self.model_name = os.getenv("EMBEDDING_NAME", "")


    def embed_text(self, text: str):
        response = requests.post(
            f"{self.base_url}/engines/llama.cpp/v1/embeddings",
            json={"input": text, "model": self.model_name}
        )
        embedding = response.json()["data"][0]["embedding"]

        return embedding