from logger import setup_logger, get_logger

logger = get_logger()


def main():
    setup_logger(
        log_dir="logs",
        log_level="INFO",
        diagnose=False,
        rotation="25 MB",
        retention="7 days",
    )

    logger.info("Starting solver application")


if __name__ == "__main__":
    main()
