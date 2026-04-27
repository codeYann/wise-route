from logger import setup_logger, get_logger
from env import get_env

logger = get_logger()


def main():
    env = get_env()
    setup_logger(
        log_level=env.log_level,
        diagnose=env.log_diagnose,
        rotation=env.log_rotation,
        retention=env.log_retention,
    )

    logger.info("Starting solver application")


if __name__ == "__main__":
    main()
