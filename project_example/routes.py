"""Routes

Contains all of the application route functions
"""
from starlette.responses import UJSONResponse
from starlette.routing import Route
from json.decoder import JSONDecodeError


async def index(req):
    """Index route
    """
    return UJSONResponse({'msg': 'Hello, world!'})


async def post_me(req):
    """Test POST route
    """
    try:
        # convert the body to json
        data = await req.json()
        return UJSONResponse({'msg': f'Hello {data["name"]}!'})
    except JSONDecodeError:
        return UJSONResponse({'msg': 'You posted nothing!!'})
    except KeyError:
        return UJSONResponse({'err': 'Please provide your name'},
                             status_code=400)


async def req_param(req):
    """Reqeuest param test
    """
    return UJSONResponse({
        'msg': f"Param = {req.path_params.get('id', -1)}"
    })


# Export the routes
routes = [
    Route('/', index, methods=['GET'], name='index'),
    Route('/postme', post_me, methods=['POST'], name='postme'),
    Route('/param/{id:int}', req_param, methods=['GET'], name='reqparam')
]
