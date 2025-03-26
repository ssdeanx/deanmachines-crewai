"""
Retry utilities for handling transient failures.
"""
import time
import logging
from functools import wraps
from typing import Callable, Any, Optional

logger = logging.getLogger(__name__)

def retry_with_backoff(
    max_attempts: int = 3,
    initial_wait: float = 1.0,
    exponential_base: float = 2.0,
    logger: Optional[logging.Logger] = None
) -> Callable:
    """
    Decorator that implements exponential backoff for retrying failed operations.

    Args:
        max_attempts: Maximum number of retry attempts (default: 3)
        initial_wait: Initial wait time in seconds (default: 1.0)
        exponential_base: Base for exponential backoff (default: 2.0)
        logger: Optional logger instance for retry logging
    """
    if logger is None:
        logger = logging.getLogger(__name__)

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(
                            f"Failed after {max_attempts} attempts. Final error: {str(e)}"
                        )
                        raise

                    wait_time = initial_wait * (exponential_base ** (attempts - 1))
                    logger.warning(
                        f"Attempt {attempts} failed: {str(e)}. "
                        f"Retrying in {wait_time:.2f} seconds..."
                    )
                    time.sleep(wait_time)
            return None
        return wrapper
    return decorator
