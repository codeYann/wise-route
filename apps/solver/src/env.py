from pydantic_settings import BaseSettings
from pathlib import Path
from functools import lru_cache
from urllib.parse import quote_plus


def find_project_root(start_path: Path) -> Path:
    current = start_path.resolve()
    for parent in [current] + list(current.parents):
        if (parent / "pnpm-workspace.yaml").exists():
            return parent
    raise RuntimeError("Could not find project root with pnpm-workspace.yaml")


ROOT_DIR = find_project_root(Path(__file__))


class Env(BaseSettings):
    rabbitmq_user: str
    rabbitmq_password: str
    rabbitmq_host: str = "localhost"
    rabbitmq_port: int = 5672

    # Logger configuration
    log_level: str = "INFO"
    log_diagnose: bool = False
    log_rotation: str = "25 MB"
    log_retention: str = "7 days"

    @property
    def rabbitmq_url(self) -> str:
        user = quote_plus(self.rabbitmq_user)
        password = quote_plus(self.rabbitmq_password)
        return f"amqp://{user}:{password}@{self.rabbitmq_host}:{self.rabbitmq_port}/"

    model_config = {
        "env_file": ROOT_DIR / ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }


@lru_cache()
def get_env() -> Env:
    return Env()
