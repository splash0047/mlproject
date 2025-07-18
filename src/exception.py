import sys 
from src.logger import logging

def error_message_details(error: Exception, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name= exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occcured in python script [{0}] at line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))

    return error_message
        
    
class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

