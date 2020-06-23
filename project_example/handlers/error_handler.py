"""Error Handler

Contains all of the application error handlers
"""
import sys
from starlette.responses import UJSONResponse
from starlette.exceptions import HTTPException


async def http_error_handler(req, exc):
    """Generic application error handler
    """
    return UJSONResponse({'err': exc.detail}, status_code=exc.status_code)


handlers = {
    HTTPException: http_error_handler
}
