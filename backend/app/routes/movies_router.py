from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.controllers import movie_controller
from app.database import get_db
from app.schemas.movie_schema import (
    ActorsWithMultipleCharactersResponse,
    CharactersWithMultipleActorsResponse,
    MoviePerActor,
)
from app.schemas.schemas import ApiPaginatedResponse

router = APIRouter(
    prefix="/api",
    tags=["Movies"]
)


@router.get("/movies-per-actor", response_model=ApiPaginatedResponse)
def get_movies_per_actor(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    limit: int = Query(20, le=100)
):
    return movie_controller.get_movies_per_actor(db, page, limit)


@router.get("/actors-with-multiple-characters", response_model=ActorsWithMultipleCharactersResponse)
def actors_with_multiple_characters(db: Session = Depends(get_db)):
    return movie_controller.get_actors_with_multiple_characters(db)


@router.get("/characters-with-multiple-actors", response_model=CharactersWithMultipleActorsResponse)
def characters_with_multiple_actors(db: Session = Depends(get_db)):
    return movie_controller.get_characters_with_multiple_actors(db)
