import os
import logging

logger = logging.getLogger(__name__)
logger.level = logging.INFO

FTC_SERVER_PORT = os.getenv("FTC_SERVER_PORT", 9001)