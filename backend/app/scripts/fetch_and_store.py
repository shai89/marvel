import os
import sys
import json
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlalchemy.orm import Session
from app.database import SessionLocal, Base, engine
from app import models
from app.dal import movie_dal, actor_dal, appearance_dal
from app.models import Character
from app.utils.tmdb_client import get_movie_details, get_movie_credits

# ----------------------------- CONFIG -----------------------------

# MOVIE_LIST_PATH = "scripts/movies.json"
MOVIE_LIST_PATH = os.path.join(os.path.dirname(__file__), "movies.json")

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# ----------------------------- HELPERS -----------------------------

def load_movie_list(path: str):
    """Load list of TMDB movie IDs and titles from JSON file."""
    with open(path, "r") as f:
        return json.load(f)

def get_or_create_character(db: Session, name: str) -> Character:
    """Ensure a character exists in the DB."""
    character = db.query(Character).filter_by(name=name).first()
    if character:
        return character
    character = Character(name=name)
    db.add(character)
    db.commit()
    db.refresh(character)
    return character

def process_movie(db: Session, tmdb_id: int, fallback_title: str = ""):
    """Fetch and store one movie and its cast."""
    try:
        movie_data = get_movie_details(tmdb_id)
        title = movie_data.get("title") or fallback_title
        logger.info(f"Processing movie: {title} (TMDB ID: {tmdb_id})")

        movie = movie_dal.get_or_create_movie(db, tmdb_id=tmdb_id, title=title)

        credits = get_movie_credits(tmdb_id)
        cast_list = credits.get("cast", [])

        for cast in cast_list:
            actor_name = cast.get("name")
            character_name = cast.get("character")

            if not actor_name or not character_name:
                continue  # Skip incomplete records

            actor = actor_dal.get_or_create_actor(db, name=actor_name)
            character = get_or_create_character(db, name=character_name)

            exists = (
                db.query(models.Appearance)
                .filter_by(
                    actor_id=actor.id,
                    movie_id=movie.id,
                    character_id=character.id
                )
                .first()
            )
            if not exists:
                appearance_dal.create_appearance(
                    db=db,
                    actor_id=actor.id,
                    movie_id=movie.id,
                    character_id=character.id
                )

    except Exception as e:
        logger.error(f"Failed to process movie {tmdb_id}: {e}")

# ----------------------------- MAIN -----------------------------

def main():
    logger.info("Initializing database...")
    Base.metadata.create_all(bind=engine)

    movies = load_movie_list(MOVIE_LIST_PATH)

    db = SessionLocal()
    try:
        for movie in movies:
            tmdb_id = movie.get("id")
            title = movie.get("title", "")
            if not tmdb_id:
                logger.warning(f"Skipping movie with missing ID: {title}")
                continue
            process_movie(db, tmdb_id, fallback_title=title)
    finally:
        db.close()

    logger.info("✅ Done.")

if __name__ == "__main__":
    main()
