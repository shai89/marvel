from sqlalchemy.orm import Session
from app import models


def get_or_create_movie(db: Session, tmdb_id: int, title: str):
    movie = db.query(models.Movie).filter(models.Movie.tmdb_id == tmdb_id).first()
    if movie:
        return movie

    movie = models.Movie(title=title, tmdb_id=tmdb_id)
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie


def get_all_movies(db: Session):
    return db.query(models.Movie).all()
