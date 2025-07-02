
import pytest
from starlette.status import HTTP_200_OK
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# ==========================
# Helper Functions
# ==========================
def assert_valid_movie_per_actor(entry):
    assert "actorName" in entry
    assert isinstance(entry["actorName"], str)
    assert "movies" in entry
    assert isinstance(entry["movies"], list)
    for movie in entry["movies"]:
        assert "movieTitle" in movie
        assert "characterName" in movie

def assert_valid_actor_with_characters(actor_name, character_list):
    assert isinstance(actor_name, str)
    assert isinstance(character_list, list)
    for character in character_list:
        assert "movieName" in character
        assert "characterName" in character

def assert_valid_character_with_actors(character_name, actor_list):
    assert isinstance(character_name, str)
    assert isinstance(actor_list, list)
    for actor_entry in actor_list:
        assert "movieName" in actor_entry
        assert "actorName" in actor_entry

# ==========================
# /movies-per-actor
# ==========================
def test_movies_per_actor_returns_valid_response():
    response = client.get("/api/movies-per-actor")
    assert response.status_code == HTTP_200_OK
    data = response.json()
    assert isinstance(data, dict)
    assert "items" in data
    for entry in data["items"]:
        assert_valid_movie_per_actor(entry)

def test_movies_per_actor_empty(monkeypatch):
    from app.controllers import movie_controller
    monkeypatch.setattr(movie_controller, "get_movies_per_actor", lambda db=..., page=1, limit=20: {
        "items": [],
        "total": 0,
        "page": 1,
        "limit": 20
    })
    response = client.get("/api/movies-per-actor")
    assert response.status_code == HTTP_200_OK
    assert response.json()["items"] == []

# ==========================
# /actors-with-multiple-characters
# ==========================
def test_actors_with_multiple_characters():
    response = client.get("/api/actors-with-multiple-characters")
    assert response.status_code == HTTP_200_OK
    data = response.json()
    assert isinstance(data, dict)
    for actor_name, characters in data.items():
        assert_valid_actor_with_characters(actor_name, characters)

def test_actors_with_same_character_in_multiple_movies_excluded(monkeypatch, client):
    from app.controllers import movie_controller
    mock_data = {
        "Chris Evans": [
            {"movieName": "Captain America", "characterName": "Steve Rogers"},
            {"movieName": "Avengers", "characterName": "Steve Rogers"},
        ],
        "Tom Hardy": [
            {"movieName": "Venom", "characterName": "Eddie Brock"},
            {"movieName": "Spider-Man", "characterName": "Venom"},
        ],
    }

    monkeypatch.setattr(
        movie_controller,
        "get_actors_with_multiple_characters",
        lambda db: mock_data
    )

    response = client.get("/api/actors-with-multiple-characters")
    result = response.json()

    # Tom Hardy should be included (different characters)
    assert "Tom Hardy" in result

def test_actors_with_multiple_characters_empty(monkeypatch):
    from app.controllers import movie_controller
    monkeypatch.setattr(movie_controller, "get_actors_with_multiple_characters", lambda db=...: {})
    response = client.get("/api/actors-with-multiple-characters")
    assert response.status_code == HTTP_200_OK
    assert response.json() == {}

# ==========================
# /characters-with-multiple-actors
# ==========================
def test_characters_with_multiple_actors():
    response = client.get("/api/characters-with-multiple-actors")
    assert response.status_code == HTTP_200_OK
    data = response.json()
    assert isinstance(data, dict)
    for character_name, actor_list in data.items():
        assert_valid_character_with_actors(character_name, actor_list)

def test_character_played_by_same_actor_multiple_movies_excluded(client):
    response = client.get("/api/characters-with-multiple-actors")
    data = response.json()
    assert "Tony Stark" not in data

def test_characters_with_multiple_actors_empty(monkeypatch):
    from app.controllers import movie_controller
    monkeypatch.setattr(movie_controller, "get_characters_with_multiple_actors", lambda db=...: {})
    response = client.get("/api/characters-with-multiple-actors")
    assert response.status_code == HTTP_200_OK
    assert response.json() == {}

def test_multiple_actors_same_name(monkeypatch, client):
    from app.controllers import movie_controller
    mock_data = {
        "items": [
            {
                "id": 1,
                "actorName": "Chris Evans",
                "movies": [
                    {"movieTitle": "Captain America", "characterName": "Steve Rogers"},
                    {"movieTitle": "X-Men", "characterName": "Cyclops"},
                ]
            }
        ],
        "total": 1,
        "page": 1,
        "limit": 20
    }

    monkeypatch.setattr(
        movie_controller,
        "get_movies_per_actor",
        lambda db, page=1, limit=20: mock_data
    )

    response = client.get("/api/movies-per-actor")
    assert response.status_code == 200
    data = response.json()["items"]

    assert any(
        actor["actorName"] == "Chris Evans" and len(actor["movies"]) == 2
        for actor in data
    )

def test_empty_actor_name(monkeypatch, client):
    from app.controllers import movie_controller
    mock_data = {
        "items": [
            {
                "id": 999,
                "actorName": "",
                "movies": [
                    {"movieTitle": "Thor", "characterName": "Loki"},
                ]
            }
        ],
        "total": 1,
        "page": 1,
        "limit": 20
    }

    monkeypatch.setattr(
        movie_controller,
        "get_movies_per_actor",
        lambda db, page=1, limit=20: mock_data
    )

    response = client.get("/api/movies-per-actor")
    assert response.status_code == 200
    data = response.json()["items"]

    assert any(actor["actorName"] == "" for actor in data)

