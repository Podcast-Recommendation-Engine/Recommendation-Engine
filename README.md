# LLM-Service

## Overview

This repository contains the **LLM-Service**, a modular microservice designed to interact with **Large Language Models (LLMs)** such as **Google Gemini** or **Ollama**.  
It exposes both **REST (FastAPI)** and **gRPC** endpoints, allowing other components in the **Podcast Recommendation Platform** to leverage LLMs for tasks like text summarization, metadata generation, and semantic understanding.

The service is **containerized with Docker** for easy deployment and scalability across environments.

---

## Key Features

-  **FastAPI** RESTful interface for LLM queries  
-  Support for multiple backends — **Gemini** and **Ollama**  
-  **gRPC** interface for low-latency, high-throughput communication  
-  Fully **Dockerized** microservice  
-  Configurable authentication and rate limiting  
-  Asynchronous request handling for concurrent LLM calls  
-  Easily extendable to integrate new models or APIs  

---
