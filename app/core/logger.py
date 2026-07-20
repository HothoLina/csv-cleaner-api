import logging
from pathlib import Path

from app.core.settings import settings

# Create logs directory if it doesn't exist
Path(settings.LOG_DIR).mkdir(exist_ok=True)

logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL.upper()),
    format="%(asctime)s | %(levelname)s | %(message)s\n",
    handlers=[
        logging.FileHandler(
            Path(settings.LOG_DIR) / settings.LOG_FILE
        ),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("csv_cleaner")