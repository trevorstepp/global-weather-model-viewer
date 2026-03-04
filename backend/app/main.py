from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from core.config import settings
from db.database import create_tables

# routers
from routers.test import router as test_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup logic
    create_tables()
    yield
    # shutdown logic

app = FastAPI(
    title="Weather Model Viewer",
    description="API to view global weather models and hurricane models",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routers
app.include_router(test_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)