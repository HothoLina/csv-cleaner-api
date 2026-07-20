class CSVCleanerException(Exception):
    """
    Base exception for the CSV Cleaner application.
    """

    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class InvalidCSVError(CSVCleanerException):
    def __init__(self):
        super().__init__(
            message="The uploaded file is not a valid CSV.",
            status_code=400,
        )


class EmptyCSVError(CSVCleanerException):
    def __init__(self):
        super().__init__(
            message="The uploaded CSV contains no data.",
            status_code=400,
        )