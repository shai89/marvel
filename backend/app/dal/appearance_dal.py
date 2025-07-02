from sqlalchemy.orm import Session
from sqlalchemy import func, distinct

from app import models


def create_appearance(db: Session, actor_id: int, movie_id: int, character_id: int):
    appearance = models.Appearance(
        actor_id=actor_id,
        movie_id=movie_id,
        character_id=character_id
    )
    db.add(appearance)
    db.commit()
    db.refresh(appearance)
    return appearance


def get_all_appearances(db: Session):
    return db.query(models.Appearance).all()


def get_movies_per_actor(db: Session, page: int, limit: int):
    """
    Returns a paginated list of actors and their appearances in movies as characters.
    """
    offset = (page - 1) * limit

    rows = (
        db.query(
            models.Actor.id.label("actor_id"),
            models.Actor.name.label("actor_name"),
            models.Movie.title.label("movie_title"),
            models.Character.name.label("character_name"),
        )
        .join(models.Appearance, models.Actor.id == models.Appearance.actor_id)
        .join(models.Movie, models.Movie.id == models.Appearance.movie_id)
        .join(models.Character, models.Character.id == models.Appearance.character_id)
        .order_by(models.Actor.id)
        .offset(offset)
        .limit(limit)
        .all()
    )

    total = db.query(func.count(distinct(models.Actor.id))).scalar()

    return rows, total


def get_actors_with_multiple_characters(db: Session):
    """
    Returns a dictionary of actors who played multiple distinct characters.
    """
    actor_roles = {}

    rows = (
        db.query(models.Actor.name, models.Movie.title, models.Character.name)
        .join(models.Appearance, models.Actor.id == models.Appearance.actor_id)
        .join(models.Movie, models.Movie.id == models.Appearance.movie_id)
        .join(models.Character, models.Character.id == models.Appearance.character_id)
        .all()
    )

    for actor_name, movie_title, character_name in rows:
        actor_roles.setdefault(actor_name, []).append({
            "movieName": movie_title,
            "characterName": character_name
        })

    return {
        actor_name: appearances
        for actor_name, appearances in actor_roles.items()
        if len(set(a["characterName"] for a in appearances)) > 1
    }


def get_characters_with_multiple_actors(db: Session):
    """
    Returns a dictionary of characters who were played by multiple actors.
    """
    character_roles = {}

    rows = (
        db.query(models.Character.name, models.Movie.title, models.Actor.name)
        .join(models.Appearance, models.Character.id == models.Appearance.character_id)
        .join(models.Movie, models.Movie.id == models.Appearance.movie_id)
        .join(models.Actor, models.Actor.id == models.Appearance.actor_id)
        .all()
    )

    for character_name, movie_title, actor_name in rows:
        character_roles.setdefault(character_name, []).append({
            "movieName": movie_title,
            "actorName": actor_name
        })

    return {
        character_name: appearances
        for character_name, appearances in character_roles.items()
        if len(set(a["actorName"] for a in appearances)) > 1
    }
