"""FastAPI application entry point."""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.database import Base, engine
from app.routers import auth, books, loans


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=settings.app_name,
    description="REST API for a small library: catalogue search, member accounts with JWT auth, "
                "and borrowing/returning with loan limits and overdue tracking.",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(auth.router)
app.include_router(books.router)
app.include_router(loans.router)


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}
