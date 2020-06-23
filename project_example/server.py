"""Starlette Tutorial

Basic Starlette project
"""
from starlette.applications import Starlette
from starlette.routing import Mount
import uvicorn

import handlers.event_handlers as eh
from settings import DEBUG
from handlers.error_handler import handlers
from routes import routes
from middleware import middleware

route_table = [
    Mount('/', routes=routes, name='routes')
]

app = Starlette(debug=DEBUG,
                routes=route_table,
                middleware=middleware,
                exception_handlers=handlers,
                on_startup=[eh.startup],
                on_shutdown=[eh.shutdown])

if __name__ == '__main__':
    uvicorn.run('server:app', port=8000, reload=True)
