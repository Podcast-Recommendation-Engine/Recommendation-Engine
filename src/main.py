from fastapi import FastAPI, Body
from fastapi.responses import Response
from src.routers.embedding import router as embedding_router
from src.routers.videos_recommendation import router as videos_recommendation_router

app = FastAPI(title="Podcast Recommendation Engine API")

# Include the routers
app.include_router(embedding_router)
app.include_router(videos_recommendation_router)
