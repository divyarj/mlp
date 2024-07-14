import sys

def error_messgae_details(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message='Error in script [{0}] :: line [{1}] :: error message :: [{2}]'.format(file_name,
                                                                                         exc_tb.tb_frame.f_lineno,
                                                                                         str(error))
    return error_message
    
class CustomerException(Exception):
    def __init__(self, error_message, error_detail:sys) -> None:
        super().__init__(error_message)
        self.error_message = error_messgae_details(error_message, error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message
