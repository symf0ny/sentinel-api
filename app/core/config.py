from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = 'Sentinel APP'
    app_description: str = 'Website and API monitoring service'
    app_version: str = '0.1.0'
    debug: bool = False

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
