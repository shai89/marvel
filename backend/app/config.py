import os
from dotenv import load_dotenv
load_dotenv()
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    USE_SQLITE: bool = False
    TMDB_API_TOKEN: str

    class Config:
        env_file = ".env"

settings = Settings()