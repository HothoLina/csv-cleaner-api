from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import CSVCleanerException
from app.core.logger import logger


async def csv_exception_handler(
    request: Request,
    exc: CSVCleanerException,
):
    """
    Handle custom application exceptions.
    """

    logger.error(exc.message)

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "type": exc.__class__.__name__,
                "message": exc.message,
            },
        },
    )


async def unexpected_exception_handler(
    request: Request,
    exc: Exception,
):
    """
    Handle unexpected exceptions.
    """

    logger.exception(str(exc))

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": {
                "type": "InternalServerError",
                "message": "An unexpected error occurred.",
            },
        },
    )