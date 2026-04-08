# device_connection.py
# device_connection.py
# Module for checking if a provided path (e.g., mounted Android media) is accessible
# Usage: import is_device_accessible from this module
# No direct execution; use in main app or test with pytest

import os
from loguru import logger

def is_device_accessible(media_path: str) -> bool:
    """
    Returns True if the provided media_path exists and is accessible, else False.
    """
    try:
        if os.path.exists(media_path) and os.path.isdir(media_path):
            logger.debug(f"Media path accessible: {media_path}")
            return True
        else:
            logger.warning(f"Media path not accessible: {media_path}")
            return False
    except Exception as e:
        logger.error(f"Error checking media path: {e}")
        return False

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python device_connection.py <media_path>")
        exit(1)
    path = sys.argv[1]
    if is_device_accessible(path):
        logger.success(f"Media path is accessible: {path}")
    else:
        logger.warning(f"Media path is not accessible: {path}")