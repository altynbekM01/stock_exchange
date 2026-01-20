from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List



class Settings(BaseSettings):
    DATABASE_URL: str
    DERIBIT_BASE_URL: str
    REDIS_URL: str
    TICKERS: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore", 
    )

    @property
    def tickers(self) -> List[str]:
        return [t.strip() for t in self.TICKERS.split(",")]



settings = Settings()

