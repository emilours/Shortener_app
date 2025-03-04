from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """ Settings for the application """
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortener.db"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    """ Retrieve cached application settings """
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
