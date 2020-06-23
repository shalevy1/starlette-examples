# server.py
from starlette.applications import Starlette
from starlette.responses import UJSONResponse
from starlette.routing import Route
from starlette.background import BackgroundTask
import uvicorn
from json import JSONDecodeError


async def save_email(email):
    """Saves email to disk
    """
    print(f'saving email {email} to disk...')
    with open('emails.csv', 'a') as f:
        f.write(email + ',\n')

    print('done')


async def add_email(req):
    """Contact API route

    User posts an email and the application then writes this to file in a 
    background task.
    """
    try:
        data = await req.json()

        # create response with background task to run once sent
        return UJSONResponse({
            'msg': 'Saving email address'
        }, background=BackgroundTask(save_email, email=data['email']))
    except (JSONDecodeError, KeyError):
        return UJSONResponse({'err': 'Please provide an email'},
                             status_code=400)


# Create routing table and application
routes = [Route('/email', add_email, methods=['POST'], name='add_email')]
app = Starlette(debug=True, routes=routes)

if __name__ == '__main__':
    uvicorn.run('server:app', reload=True)
