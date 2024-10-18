from typing import Optional

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_CONNECT_TIMEZONE: Optional[str]


    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
