from pydantic import BaseSettings


class Settings(BaseSettings):
    TASKAPI_HOST: str
    TASKAPI_DATABASE: str
    TASKAPI_SECRET_KEY: str
    TASKAPI_ALGORITHM: str

    class Config:
        env_file = ".env"

settings = Settings()