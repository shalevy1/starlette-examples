"""Starlette Database Server Example

Written by Nicholas Cannon
"""
import sqlalchemy as sa
import databases  # gives asynio support for sqlalchemy
import uvicorn
from json.decoder import JSONDecodeError

from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import UJSONResponse

DB_URI = 'sqlite:///site.db'

# Set up the db tables
md = sa.MetaData()
User = sa.Table(
    'users',
    md,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(25))
)

db = databases.Database(DB_URI)


async def get_users(req):
    """Returns a list of all users
    """
    query = User.select()
    res = await db.fetch_all(query)

    return UJSONResponse({
        'users': [{'id': u.id, 'name': u.name} for u in res]
    })


async def create_user(req):
    """Creates a new user
    """
    try:
        data = await req.json()  # get request body as json (dict)

        # construct UPDATE query and execute asynchronously
        query = User.insert().values(name=data['name'])
        await db.execute(query)

        return UJSONResponse({
            'msg': f"Created new user with name {data['name']}"
        })
    except (JSONDecodeError, KeyError):
        # handle client error
        return UJSONResponse({'err': 'Please supply a name'}, status_code=400)


def db_setup():
    """DB Setup
    """
    print('setting up db')
    engine = sa.create_engine(DB_URI)
    md.create_all(bind=engine)
    print('done')


# Create application instance
app = Starlette(
    debug=True,
    routes=[
        Route('/add', create_user, methods=['POST'], name='create_user'),
        Route('/list', get_users, methods=['GET'], name='get_users')
    ],
    on_startup=[db_setup, db.connect],
    on_shutdown=[db.disconnect])

if __name__ == '__main__':
    uvicorn.run('server:app', reload=True)
