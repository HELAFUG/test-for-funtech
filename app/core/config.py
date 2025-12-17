from os import getenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"


class DBConfig(BaseModel):
    url: str = getenv(
        "DB_URL", "postgresql://postgres:postgres@localhost:5434/postgres"
    )
    echo: bool = False


class LogConfig(BaseModel):
    level: str = "INFO"
    format: str = LOG_FORMAT
    datefmt: str = "%Y-%m-%d %H:%M:%S"


class AuthConfig(BaseModel):
    secret_key: str = getenv("SECRET_KEY", "secret")
    algorithm: str = "HS256"


class APIV1(BaseModel):
    prefix: str = "/v1"


class APIConfig(BaseModel):
    prefix: str = "/api"
    v1: APIV1 = APIV1()


class Settings(BaseSettings):
    db: DBConfig = DBConfig()
    log: LogConfig = LogConfig()
    api: APIConfig = APIConfig()
    auth: AuthConfig = AuthConfig()


settings = Settings()
