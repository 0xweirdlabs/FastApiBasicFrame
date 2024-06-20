import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    A class to represent the application settings.

    Attributes
    ----------
    env : str
        the current environment (e.g., 'local', 'dev', 'prod')
    database_url : str
        the URL of the database
    """
    env: str
    database_url: str


def get_settings() -> Settings:
    """
    Load environment-specific settings.

    Returns
    -------
    Settings
        The loaded settings object
    """
    env = os.getenv("ENV", "local")
    if env == "local":
        load_dotenv(".env.local")
    elif env == "dev":
        load_dotenv(".env.dev")
    elif env == "prod":
        load_dotenv(".env.prod")

    return Settings()

settings = get_settings()
