# Recommendation-Engine

## Overview

This repository contains the **Recommendation-Engine** microservice, a core component of the **Podcast Recommendation Platform**.  
It leverages **embedding-based similarity** using the **All-Mini-Mistral model** to generate podcast recommendations based on content and user interactions.

The service exposes a **gRPC API** for efficient low-latency inference and integrates with a **vector database** (e.g., Milvus, Qdrant ) to store and query embeddings using **cosine similarity**.

---

## Key Features

-  **All-Mini-Mistral** embedding model for semantic vector representations  
-  **Cosine similarity** for matching podcast content and user interests  
-  **gRPC API** for scalable, real-time recommendations  
-  **Vector database** integration (Milvus / Qdrant )  
-  Batch and real-time embedding generation  
-  Integration-ready with upstream services (API, LLM, STT, Scrapers)  
-  Fully **Dockerized** for portability and deployment consistency  

---

