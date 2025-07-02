from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    tmdb_id = Column(Integer, unique=True, nullable=False)

    appearances = relationship("Appearance", back_populates="movie")


class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    appearances = relationship("Appearance", back_populates="actor")

    # Virtual relation for easier eager loading of movies
    movies = relationship(
        "Movie",
        secondary="appearances",
        primaryjoin="Actor.id == Appearance.actor_id",
        secondaryjoin="Appearance.movie_id == Movie.id",
        viewonly=True,
    )


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

    appearances = relationship("Appearance", back_populates="character")


class Appearance(Base):
    __tablename__ = "appearances"

    id = Column(Integer, primary_key=True, index=True)
    actor_id = Column(Integer, ForeignKey("actors.id"), nullable=False)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False)

    actor = relationship("Actor", back_populates="appearances")
    movie = relationship("Movie", back_populates="appearances")
    character = relationship("Character", back_populates="appearances")
