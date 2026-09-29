"""
ORIGIN - Main Backend Application Entrypoint
SIH26091: AI-Driven Hyper-Local Business Advisory and Financial Structuring Assistant
"""

import os
import sys

# Ensure backend root is on Python module search path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from api.router import api_router

app = FastAPI(
    title="ORIGIN - Rural Micro-Enterprise Advisory Engine",
    description="Smart India Hackathon 2026 (SIH26091): Hyper-Local Market Feasibility & Financial Structuring API",
    version="1.0.0"
)

# Enable CORS for local development and production frontends
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount all API endpoints under /api
app.include_router(api_router, prefix="/api")

# Determine path to frontend dist build
frontend_dist = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend", "dist"))

if os.path.exists(frontend_dist):
    assets_dir = os.path.join(frontend_dist, "assets")
    if os.path.exists(assets_dir):
        app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")

    @app.get("/")
    async def serve_root():
        index_file = os.path.join(frontend_dist, "index.html")
        if os.path.exists(index_file):
            return FileResponse(index_file)
        return {"status": "ORIGIN API Server running"}

    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        # Don't intercept API or docs calls
        if full_path.startswith("api/") or full_path == "docs" or full_path == "openapi.json":
            raise HTTPException(status_code=404, detail="Not Found")
        # Serve static file if exists, otherwise index.html
        requested_file = os.path.join(frontend_dist, full_path)
        if os.path.isfile(requested_file):
            return FileResponse(requested_file)
        return FileResponse(os.path.join(frontend_dist, "index.html"))
else:
    @app.get("/")
    def root_status():
        return {
            "app": "ORIGIN API Server",
            "tagline": "Your Business Idea. Your Local Market. Your Financial Plan.",
            "sih_code": "SIH26091",
            "status": "Online",
            "api_documentation": "/docs"
        }


if __name__ == "__main__":
    import uvicorn
    # Run server on port 8000
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
