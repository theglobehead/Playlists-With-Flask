from loguru import logger


class LoggingUtils:
    @staticmethod
    def log(message: str) -> None:
        logger.log("DEBUG", message, colorize=True)
