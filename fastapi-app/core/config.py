from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunConfiguration(BaseModel):
    """
    Конфигурация запуска приложения
    """

    host: str = "0.0.0.0"
    port: int = 8000


class ApiPrefix(BaseModel):
    """
    Префикс для API
    """

    prefix: str = "/api"


class Settings(BaseSettings):
    """
    Настройки приложения
    """

    run: RunConfiguration = RunConfiguration()
    api: ApiPrefix = ApiPrefix()


settings = Settings()
