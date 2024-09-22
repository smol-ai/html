from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# CORS configuration
if os.getenv("ENV") == "development":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # Vite dev server
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Serve static files in production
if os.getenv("ENV") == "production":
    app.mount("/", StaticFiles(directory="../frontend/dist", html=True), name="static")

@app.get("/api/hello")
def read_root():
    return {"message": "Hello from FastAPI"}
