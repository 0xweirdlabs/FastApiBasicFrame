import os
from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    env: str
    database_url: str


def get_settings():
    env = os.getenv("ENV", "local")
    if env == "local":
        load_dotenv(".env.local")
    elif env == "dev":
        load_dotenv(".env.dev")
    elif env == "prod":
        load_dotenv(".env.prod")

    return Settings()


settings = get_settings()
