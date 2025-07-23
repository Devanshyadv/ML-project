import sys
import logging

def error_message_details(error, error_detail: sys):
    """
    Build a detailed error message including:
      - the file where the error occurred
      - the line number of the error
      - the original error message
    """
    # exc_info() returns a tuple (type, value, traceback)
    _, _, exc_tb = error_detail.exc_info()
    # Get the filename from the traceback frame
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Construct the message
    error_message = (
        f"Error occurred in python script name [{file_name}] "
        f"line number [{exc_tb.tb_lineno}] "
        f"error message [{error}]"
    )
    return error_message


class CustomException(Exception):
    """
    A custom exception class that captures and formats error details.
    """
    def __init__(self, error_message, error_detail: sys):
        # Generate the detailed message using our helper
        detailed_message = error_message_details(error_message, error_detail)
        # Initialize the base Exception with our detailed message
        super().__init__(detailed_message)
        self.error_message = detailed_message

    def __str__(self):
        # When the exception is printed, show the detailed message
        return self.error_message


