from pydantic import BaseModel
from typing import List

# ========== Movie ==========
class MovieBase(BaseModel):
    title: str
    tmdb_id: int

class MovieCreate(MovieBase):
    pass

class MovieOut(MovieBase):
    id: int

    class Config:
        orm_mode = True

# ========== Actor ==========
class ActorBase(BaseModel):
    name: str

class ActorCreate(ActorBase):
    pass

class ActorOut(ActorBase):
    id: int

    class Config:
        orm_mode = True


class ActorWithMoviesOut(ActorOut):
    movies: List[MovieOut]

    class Config:
        orm_mode = True

# ========== Character ==========
class CharacterBase(BaseModel):
    name: str

class CharacterCreate(CharacterBase):
    pass

class CharacterOut(CharacterBase):
    id: int

    class Config:
        orm_mode = True

# ========== Appearance ==========
class AppearanceOut(BaseModel):
    id: int
    actor: ActorOut
    movie: MovieOut
    character: CharacterOut

    class Config:
        orm_mode = True

class MovieOut(BaseModel):
    movieTitle: str
    characterName: str

class ActorWithMoviesOut(BaseModel):
    id: int
    actorName: str
    movies: List[MovieOut]


class ApiPaginatedResponse(BaseModel):
    items: List[ActorWithMoviesOut]
    total: int
    page: int
    limit: int
