import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    """Extracts detailed error information."""
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        f"Error occurred in python script name [{file_name}] "
        f"line number [{exc_tb.tb_lineno}] "
        f"error message [{str(error)}]"
    )
    return error_message

class CustomException(Exception):
    """Custom exception class for detailed error handling."""

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.error("An exception occurred: %s", str(e))
        raise CustomException(e, sys) from e
