import requests
from typing import Dict, Any, List
from app.config import settings

TMDB_API_URL = "https://api.themoviedb.org/3"
HEADERS = {
    "Authorization": f"Bearer {settings.TMDB_API_TOKEN}"
}

def get_movie_details(tmdb_id: int) -> Dict[str, Any]:
    """
    Fetch basic movie info by TMDB ID.
    """
    url = f"{TMDB_API_URL}/movie/{tmdb_id}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()


def get_movie_credits(tmdb_id: int) -> Dict[str, Any]:
    """
    Fetch cast and crew info for a given movie.
    """
    url = f"{TMDB_API_URL}/movie/{tmdb_id}/credits"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()


def search_person_by_name(name: str) -> List[Dict[str, Any]]:
    """
    Search for a person (actor) by name.
    """
    url = f"{TMDB_API_URL}/search/person"
    params = {"query": name}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json().get("results", [])
