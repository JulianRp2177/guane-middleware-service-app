import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    WEB_APP_VERSION : str = os.getenv("WEB_APP_VERSION")
    WEB_APP_TITLE: str = os.getenv("WEB_APP_TITLE")
    WEB_APP_DESCRIPTION: str = os.getenv("WEB_APP_DESCRIPTION")
    SERVICE_DATABASE: str = os.getenv("DATABASE")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT")
    DEBUGGER: bool = os.getenv("DEBUGGER")
    WORKER_API: str = os.getenv("WORKER_API")


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("loading environment variables. ")
    return Settings()

    
settings: Settings = get_settings()