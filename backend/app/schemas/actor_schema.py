from typing import List
from pydantic import BaseModel


class MovieSchema(BaseModel):
    title: str
    character: str

    class Config:
        orm_mode = True


class ActorWithMoviesSchema(BaseModel):
    actor_name: str
    movies: List[MovieSchema]

    class Config:
        orm_mode = True
