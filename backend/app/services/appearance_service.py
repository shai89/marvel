from sqlalchemy.orm import Session
from app.dal import appearance_dal
import logging

logger = logging.getLogger(__name__)


def get_movies_per_actor_service(db: Session, page: int, limit: int) -> dict:
    """
    Returns a paginated list of actors with their movies and character names.
    """
    try:
        logger.debug("Querying DB for movies per actor (page=%d, limit=%d)", page, limit)
        rows, total = appearance_dal.get_movies_per_actor(db, page, limit)

        grouped = {}
        for row in rows:
            actor_id = row.actor_id
            actor_name = row.actor_name
            movie = {
                "movieTitle": row.movie_title,
                "characterName": row.character_name
            }

            if actor_id in grouped:
                grouped[actor_id]["movies"].append(movie)
            else:
                grouped[actor_id] = {
                    "id": actor_id,
                    "actorName": actor_name,
                    "movies": [movie]
                }

        logger.info("Fetched %d actors with movies", len(grouped))
        return {
            "items": list(grouped.values()),
            "total": total,
            "page": page,
            "limit": limit,
        }

    except Exception as e:
        logger.exception("Error in get_movies_per_actor_service: %s", e)
        raise


def get_actors_with_multiple_characters_service(db: Session) -> dict:
    """
    Returns actors who played more than one character.
    """
    try:
        logger.debug("Querying DB for actors with multiple characters")
        return appearance_dal.get_actors_with_multiple_characters(db)
    except Exception as e:
        logger.exception("Error in get_actors_with_multiple_characters_service: %s", e)
        raise


def get_characters_with_multiple_actors_service(db: Session) -> dict:
    """
    Returns characters played by more than one actor.
    """
    try:
        logger.debug("Querying DB for characters with multiple actors")
        return appearance_dal.get_characters_with_multiple_actors(db)
    except Exception as e:
        logger.exception("Error in get_characters_with_multiple_actors_service: %s", e)
        raise
