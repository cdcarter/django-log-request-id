import logging
from log_request_id import current_request_var, NO_REQUEST_ID


class RequestIDFilter(logging.Filter):

    def filter(self, record):
        record.request_id = current_request_var.get(NO_REQUEST_ID)
        return True
