from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application configuration settings"""

    # Application settings
    app_name: str = "MyApp Backend"
    environment: str = "local"

    # Database settings
    db_host: str = "localhost"
    db_port: int = 3306
    db_name: str = "myappdb"
    db_username: str = "root"
    db_password: str = ""

    # Server settings
    server_port: int = 8080

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

    @property
    def database_url(self) -> str:
        """Construct database URL for SQLAlchemy"""
        if self.environment == "local":
            return f"mysql+pymysql://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        return f"mysql+pymysql://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


# Global settings instance
settings = Settings()
