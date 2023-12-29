from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    app_name: str = "main"
    title: str = "MAIN"
    docs_url: str = "/"
    env_file: str = ".env"


class UvicornSettings(BaseSettings):
    reload: bool = True
    host: str = "127.0.0.1"
    port: int = 8000
    workers: int = 1
    log_level: str = "debug"
