class FailedTelegramResponse(Exception):
    def __init__(self, error_code):
        msg = "Failed response, error code " + str(error_code)
        super(FailedTelegramResponse, self).__init__(msg)