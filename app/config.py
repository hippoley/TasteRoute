from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    qloo_api_key: str | None = None
    qloo_base_url: str = "https://hackathon.api.qloo.com"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
