from fastapi import FastAPI
from app.database import init_db
from app.routes.movies_router import router as movies_router
from app.middlewares.cors import add_cors_middleware

app = FastAPI(
    title="Marvel Movie Explorer",
    version="1.0.0",
    description="Explore Marvel movies, actors, and characters via TMDB",
)

# Attach CORS middleware
add_cors_middleware(app)

# Register routers
app.include_router(movies_router, tags=["Movies"])

# DB setup
@app.on_event("startup")
def on_startup():
    init_db()
