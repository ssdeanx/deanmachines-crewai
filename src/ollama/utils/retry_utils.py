import time
from typing import Callable, Any, Dict
from functools import wraps
import logging

logger = logging.getLogger(__name__)

def retry_with_backoff(
    retries: int = 3,
    backoff_factor: float = 2,
    initial_delay: float = 1,
    exceptions: tuple = (Exception,)
):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = initial_delay
            last_exception = None

            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < retries - 1:
                        sleep_time = delay * (backoff_factor ** attempt)
                        logger.warning(
                            f"Attempt {attempt + 1} failed: {str(e)}. "
                            f"Retrying in {sleep_time:.2f} seconds..."
                        )
                        time.sleep(sleep_time)
                    continue

            logger.error(f"All {retries} attempts failed. Last error: {str(last_exception)}")
            raise last_exception

        return wrapper
    return decorator
