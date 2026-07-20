import os

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Settings:
    """
    Application configuration.
    """

    UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")

    LOG_DIR = os.getenv("LOG_DIR", "logs")

    LOG_FILE = os.getenv("LOG_FILE", "app.log")

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    MAX_UPLOAD_SIZE = int(
        os.getenv("MAX_UPLOAD_SIZE", 10485760)
    )


settings = Settings()