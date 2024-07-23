"""Setting Module"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Setting class"""
    MS_NAME: str = "n5-challenge"
    API_PREFIX: str = "api/v1"
    API_STR: str = f"/{MS_NAME}/{API_PREFIX}"

    model_config = SettingsConfigDict(env_file="../.env")


settings = Settings()
