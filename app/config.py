from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:pass@db:5432/metrics"
    DEFAULT_CAC: float = 500
    DEFAULT_GROSS_MARGIN: float = 0.80
    class Config:
        env_file = ".env"

settings = Settings()
