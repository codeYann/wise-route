import sys
from pathlib import Path
from loguru import Logger, logger

DEFAULT_LOG_DIR = Path(__file__).parent.parent / "logs"


def setup_logger(
    log_dir: Path | str | None = None,
    log_level: str = "INFO",
    diagnose: bool = False,
    rotation: str = "25 MB",
    retention: str = "7 days",
) -> None:
    """
    Configure application logger.

    Args:
        log_dir: Directory to store log files (defaults to apps/solver/logs)
        log_level: Minimum log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        diagnose: If True, display variable values in exceptions (disable in production)
        rotation: Condition to rotate log file
        retention: Retention time for old log files
    """
    logger.remove()

    log_path = Path(log_dir) if log_dir else DEFAULT_LOG_DIR
    log_path.mkdir(exist_ok=True, parents=True)

    logger.add(
        sys.stderr,
        level=log_level,
        colorize=True,
        format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        backtrace=True,
        diagnose=diagnose,
    )

    logger.add(
        log_path / "app.log",
        level=log_level,
        rotation=rotation,
        retention=retention,
        compression="gz",
        encoding="utf-8",
        enqueue=True,
        backtrace=True,
        diagnose=diagnose,
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
    )


def get_logger() -> Logger:
    """
    Return configured logger instance.

    Returns:
        Logger: Loguru logger instance
    """
    return logger
