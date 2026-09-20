import sys

from loguru import logger


def setup_logger(log_level: str = "INFO") -> None:
    """Configures console and file logging."""
    logger.remove()

    # Console output
    logger.add(
        sys.stderr,
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level:7}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        ),
        level=log_level,
    )
