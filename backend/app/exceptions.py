from sqlite3 import IntegrityError
from fastapi.responses import JSONResponse


def generic_exception_handler(exc: Exception):
    message = "An unexpected error occurred."
    status_code = 500

    if isinstance(exc, HttpException):
        status_code = exc.status_code
        message = exc.detail

    if isinstance(exc, IntegrityError):
        status_code = 400
        message = "Record already exists"

    return JSONResponse(
        status_code=status_code,
        content={"detail": message},
    )

class HttpException(Exception):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail

class DoesNotExistError(HttpException):
    def __init__(self, detail: str = "The requested resource does not exist."):
        super().__init__(status_code=404, detail=detail)