from typing import List, Dict
from pydantic import BaseModel, RootModel


# For /movies-per-actor -----
class MoviePerActor(BaseModel):
    actorName: str
    movieTitle: str
    characterName: str


# For /actors-with-multiple-characters -----
class ActorWithCharacter(BaseModel):
    movieName: str
    characterName: str

class ActorsWithMultipleCharactersResponse(
    RootModel[Dict[str, List[ActorWithCharacter]]]
):
    """
    Example:
    {
        "Johnny Depp": [
            { "movieName": "Pirates", "characterName": "Jack Sparrow" },
            { "movieName": "Alice", "characterName": "Mad Hatter" }
        ]
    }
    """
    pass


# For /characters-with-multiple-actors -----
class CharacterWithActor(BaseModel):
    movieName: str
    actorName: str

class CharactersWithMultipleActorsResponse(
    RootModel[Dict[str, List[CharacterWithActor]]]
):
    """
    Example:
    {
        "Batman": [
            { "movieName": "The Dark Knight", "actorName": "Christian Bale" },
            { "movieName": "Batman", "actorName": "Michael Keaton" }
        ]
    }
    """
    pass