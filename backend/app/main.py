from fastapi import FastAPI
from contextlib import asynccontextmanager

from backend.app.routers import auth_routes, users_routes, posts_routes, likes_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup operations
    print("Application starting...")

    yield

    # Shutdown operations
    print("Application shutting down...")


app = FastAPI(
    title="Instagram Clone API",
    description="Backend API for Instagram Clone",
    version="1.0.0",
    lifespan=lifespan,
)


# Register routers
app.include_router(auth_routes.router)
app.include_router(users_routes.router)
app.include_router(posts_routes.router)
app.include_router(likes_routes.router)
# app.include_router(comments.router)
# app.include_router(likes.router)


@app.get("/")
async def root():
    return {"message": "Instagram Clone API is running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
