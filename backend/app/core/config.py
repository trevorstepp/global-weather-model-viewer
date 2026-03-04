from pydantic import BeforeValidator
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict
from typing import Annotated

def split_origins(v: str):
    if not v:
        return []
    if isinstance(v, str):
        return [origin.strip() for origin in v.split(",")]
    return v

class Settings(BaseSettings):
    DATABASE_URL: str
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    ALLOWED_ORIGINS: Annotated[list[str], NoDecode, BeforeValidator(split_origins)]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

settings = Settings()