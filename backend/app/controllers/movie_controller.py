from fastapi import Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.appearance_service import (
    get_movies_per_actor_service,
    get_actors_with_multiple_characters_service,
    get_characters_with_multiple_actors_service,
)
import logging

logger = logging.getLogger(__name__)


def get_movies_per_actor(
    db: Session = Depends(get_db),
    page: int = 1,
    limit: int = 20
):
    """
    Endpoint: /api/movies-per-actor?page={page}&limit={limit}
    Returns paginated list of actors with their movies and roles.
    """
    try:
        logger.info("Fetching movies per actor (page=%d, limit=%d)", page, limit)
        result = get_movies_per_actor_service(db, page, limit)

        if not result["items"]:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No actors found"
            )

        return JSONResponse(status_code=status.HTTP_200_OK, content=result)

    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Failed to fetch movies per actor: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )


def get_actors_with_multiple_characters(db: Session = Depends(get_db)):
    """
    Endpoint: /api/actors-with-multiple-characters
    Returns actors who played multiple characters.
    """
    try:
        logger.info("Fetching actors with multiple characters")
        result = get_actors_with_multiple_characters_service(db)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No such actors found"
            )

        return JSONResponse(status_code=status.HTTP_200_OK, content=result)

    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Failed to fetch actors with multiple characters: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )


def get_characters_with_multiple_actors(db: Session = Depends(get_db)):
    """
    Endpoint: /api/characters-with-multiple-actors
    Returns characters portrayed by more than one actor.
    """
    try:
        logger.info("Fetching characters with multiple actors")
        result = get_characters_with_multiple_actors_service(db)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No such characters found"
            )

        return JSONResponse(status_code=status.HTTP_200_OK, content=result)

    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Failed to fetch characters with multiple actors: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
