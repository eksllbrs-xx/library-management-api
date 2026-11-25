"""Application settings loaded from environment variables (or a .env file)."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Library Management API"
    database_url: str = "sqlite:///./library.db"
    secret_key: str = "change-me-in-production"
    access_token_expire_minutes: int = 60
    loan_days: int = 14
    max_active_loans: int = 3


settings = Settings()
