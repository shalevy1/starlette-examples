"""Middleware

Custom class based middleware example
"""
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware


class CustomLogger(BaseHTTPMiddleware):
    """CustomLogger

    Logs a message to stdout for every request in the stack.
    """

    def __init__(self, app, msg='', dispatch=None):
        super().__init__(app, dispatch=dispatch)
        self.msg = msg

    async def dispatch(self, req, call_next):
        print(f'CUSTOM LOGGER -> {self.msg}')
        return await call_next(req)


middleware = [
    Middleware(CustomLogger, msg={'msg': 'My log message!'})
]
