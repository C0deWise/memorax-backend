from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # ConfiguraciÃ³n general
    debug: bool = False
    
    POSTGRES_USER: str = "user"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "memorax_db"
    # Base de Datos
    database_url: str = "postgresql+asyncpg://user:password@localhost:5432/memorax_db"
    ALEMBIC_DATABASE_URL: str = "postgresql+psycopg://user:password@localhost:5432/memorax_db"
    # JWT Secret
    secret_key: str = "my_secret_key_here"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Supabase
    supabase_url: str = ""
    supabase_key: str = ""
    supabase_bucket: str = "memorax-storage"

    class Config:
        env_file = ".env"

settings = Settings()